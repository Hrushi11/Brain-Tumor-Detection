dir = "lgg-mri-segmentation/kaggle_3m"

# To call the corresponding original file
def tiff_call(content):
  content = content.split(".")[0] + ".tif"
  dir_ = "_".join(content.split("_")[:4])
  path = dir + "/" + dir_ + "/" + content
  return path