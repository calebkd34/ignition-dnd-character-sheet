def TotalBucket(bucket, simple):
	
	# translate values
	bucket = dict(bucket)
	simple = dict(simple)
	
	# values
	total = 0
	base = 0
	multiplier = 1
	addedProficiency = False
	
	# add each bucket value
	for key in bucket.keys():
		
		# add simple values
		if value in simple.keys():
			
			# only add proficiency bonus once
			if key == "proficiency":
				if not addedProficiency: 
					addedProficiency = False
					total += simple[value]
			
			# add it without thinking about it
			else:
				total += simple[value]
		
		# add raw values
		else:
			total += bucket[key]
			
	return total