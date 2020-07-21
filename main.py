import tinify

tinify.key = "XzwnvqRBFSBMsdFZwVNHYJ6PkgN6Hcrj"

#------------------FOR SINGE IMAGE-------------------------------
# source = tinify.from_file("mark1.jpg")
# source.to_file("mark.jpg")

#-----------------CHANGE WIDTH AND HEIGHT-------------------------------

source = tinify.from_file("mark1.jpg")
resized = source.resize(
    method="fit",
    width=500,
    height=500
)
resized.to_file("mark.jpg")

