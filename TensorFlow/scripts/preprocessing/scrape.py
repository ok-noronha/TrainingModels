from bing_image_downloader import downloader
#"Car":50,"Car front":50, "Car rear":50,"Car side":50,"Car top":50,"Indian car":50,
images = {"Indian car front":50, "Indian car rear":50,"Indian car side":50,"Indian car top":50,}
for key in images.keys():
	downloader.download(key, limit=images[key],  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)