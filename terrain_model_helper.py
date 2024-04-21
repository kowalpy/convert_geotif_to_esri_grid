import rasterio


class GeoTiffToEsriGrid:
    def __init__(self, src_file, dst_file=None, print_debug=False):
        self.header = ""
        self.src_tif = src_file
        if dst_file:
            self.dst_asc = dst_file
        else:
            self.dst_asc = f"{self.src_tif}converted.asc"
        self.print_debug = print_debug
        self.geo_tiff_data = None
        self.width = None
        self.height = None

    def create_esri_header(self, width, height):
        self.header = f"ncols {width}\n"
        self.header += f"nrows {height}\n"
        self.header += "xllcorner     0.0\nyllcorner     0.0\ncellsize      1.0\nNODATA_value  -9999\n"

    def convert(self):
        self.read_geotif()
        self.create_esri_header(self.width, self.height)
        self.save_esri_grid_contents()

    def read_geotif(self):
        with rasterio.open(self.src_tif) as src:
            self.width = src.width
            self.height = src.height
            if self.print_debug:
                print(self.width, self.height)
                print(src.crs)
                print(src.transform)
                print(src.count)
                print(src.indexes)
            self.geo_tiff_data = src.read(1)

    def save_esri_grid_contents(self):
        with open(self.dst_asc, "w") as f:
            f.write(self.header)
            for i, row in enumerate(self.geo_tiff_data):
                if self.print_debug:
                    print(f"Processing row {i}")
                    print(row)
                for cell in row:
                    f.write(f"{cell} ")
                f.write("\n")
