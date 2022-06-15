from bing_image_downloader import downloader
images = {"Car":10,"Car front":10, "Car rear":10,"Car side":10,"Car top":10,"Car under 15 lakh":10,"Car under 15 lakh front":10, "Car under 15 lakh rear":10,"Car under 15 lakh side":10,"Car under 15 lakh top":10,"Indian car":10,"Indian car front":10, "Indian car rear":10,"Indian car side":10,"Indian car top":10,}
for key in images.keys():
	downloader.download(key, limit=images[key],  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)