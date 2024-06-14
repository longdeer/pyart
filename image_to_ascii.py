from numpy		import array	as nparray
from numpy		import average	as npavg
from numpy		import float64	as npfloat
from PIL		import Image
from argparse	import ArgumentParser
from sys		import exit








GRAY_SCALES = {

	"10"	: " .:-=+*#%@",
	"20"	: " .,_-~=+:;><!?%#&$@B",
	"70"	: "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
	"10_I"	: "@%#*+=-:. ",
	"20_I"	: "B@$&#%?!<>;:+=~-_,. ",
	"70_I"	: " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",
}








class ARTASCII:

	"""
		                                                                                                             
		                                                                                                           
		                                               .,_-~==++++=~-_.                                            
		                                       ,_~=:;><<<<<<<<<<<<<<<<<;~.                                         
		                                  ,-+;><<<<<<<<<<<<<<<<<<<<<<<<<<>_                                        
		                              .-+>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<?=-                                       
		                            ,+>>>>>;><<<<<<<<<<<<<<<<<<<<<<<<<<<<?=~~,                                     
		                           =;>>>:=---:<<<<<<<<<<<<<<<<<<<<<<<<<<<?=~~~-                                    
		                          _;>>>>--__-;<<<<<<<<<<<<<<<<<<<<<<<<<<<?~~~~~                                    
		                          =;>>>>:++:><<<<<<<<<<<<<<<<<<<<<<<<<<<<?~~~~~     ._-~++=~-.                     
		                          :;>>>>>>>>>>>>;;:+;<<<<<<<<<<<<<<<<<<<<?~~~->!?#&$$$$$$$$$$$&!+.                 
		                         .;;;::++==~~---__--;<<<<<<<<<<<<<<<<<<<<!~-_,?$$$$$$$$$$$$$$$$$$$<,               
		                          ,___--~~==+::;>><<<<<<<<<<<<<<<<<<<<<<<!-__,?$$$$$$$$$$$$$$$$$$$$$:              
		                  .,,_-~=++:;;>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<-_,.?$$$$$$$$$$$$$$$$$$$$$$>             
		             ._=:;;;;;;;;;;;;>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<>-_,.%$$$$$$$$$$$$$$$$$$$$$$$>            
		           ,=:;;;;;;;;;;;;;;;>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<=-_,.%$$$$$$$$$$$$$$$$$$$$$$$&;           
		         .=::;;;;;;;;;;;;;;;;>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<>=-__,_$$$$$$$$$$$$$$$$$$$$$$$$@%;          
		        _::::;;;;;;;;;;;;;;;;;>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>:~-__,,!$$$$$$$$$$$$$$$$$$$$$$$$$&!=         
		       -::::::;;;;;;;;;;;;;;;;;>>>>>>>>>>>>>>>><<<<<<<<<<<>;+~--__,_!$$$$$$$$$$$$$$$$$$$$$$$$$$$?!,        
		      ,:::::::;;;;;;;;;;;;;;;;;>>>>>>>>>>>>>>>>>>>>>>;;:+=~--___,,:&$$$$$$$$$$$$$$$$$$$$$$$$$$$$?!+        
		      ::::::::;;;;;;;;;;;;;;;;;;;;;;;;:::+++==~~~~----______,,_+<&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$?!<        
		     -:::::::::;;;;;;;;;;;;:+=~~-----________,,,__-~~=+::;><?&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$?!!        
		     ::::::::::;;;;;;;;;:=~---___-=+:;><<!?%%#&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&!!!,       
		    ,::::::::::;;;;;;;:=---__+>%&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#!!!,       
		    -:::::::::::;;;;;:~---->&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&?!!!        
		    =:::::::::::;;;;;~--_:&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%!!!;        
		    =::::::::::::;;;:--_:$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%!!!!-        
		    -:::::::::::::;;=--~&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%!!!!:         
		    ,::::::::::::::;~-_;$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#!!!!!;          
		     -::::::::::::::--_!$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&#!<<!!!=           
		      _+:::::::::::+--_&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&#%?<<<<<<:,            
		        _~+::::++++=-_~$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&#######%%%%%%%?????!<<<<<<<<;~.              
		             .,_--~~~~;$$$$$$$$$$$$$$$$$$$$$%!<>>;;;;;;;:::::::::::;;;>>>>>>>>;;;;;;:+=~_                  
		                      <$$$$$$$$$$$$$$$$$$$$$#%??!!!!!!!!??????%%%%%%>+-.                                   
		                      #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&!!!<>_                                 
		                     _$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&!!!!!-                                 
		                     +$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&%?!!?&$$$$$$$&!!!!!-                                 
		                     <$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#!<>:+=:$$$$$$$&!!!!!-                                 
		                     ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&!<;+=~:$$$$$$$&!!!!!-                                 
		                     +$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&%?<<?$$$$$$$$%!!!!!-                                 
		                      :&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%!!!!!>                                  
		                       _<&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&#?!!!!!+                                   
		                         .=<#&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&#?!<<<<;=.                                    
		                             .-=;<!%#&&&&&&$$$$$&&&&&##%%?!<<<>;+~_                                        
		                                       .,,,__-----------__,,. 
	"""


	def to_file(
					self,
					source_image_path	:str,
					target_path			:str,
					columns_number		:int	=110,
					font_scale			:float	=.43,
					gray_scale_variant	:str	=GRAY_SCALES["10"],
				)-> str or None			:

		"""
			Convert "source_image_path" image to ascii and save it to "target_path" 
		"""

		try:

			self.to_text(source_image_path, columns_number, font_scale, gray_scale_variant)
			self.save_probe(target_path)


			return	target_path
		except		Exception as E: print(f"Failed to make ascii due to: \"{E}\"")




	def save_probe(self, target_path :str) -> str or None :

		"""
			Save ascii text as a file "target_path" and retiurn this path.
			If probe was not made, corresponing message will be printed.
		"""

		try:

			with open(target_path, "w") as tmpout:

				tmpout.write(self.probe)
				return	target_path
		except:	print("ASCII not ready yet, or file can't be created")




	def to_text(
				self,
				source_image_path	:str,
				columns_number		:int	=110,
				font_scale			:float	=.43,
				gray_scale_variant	:str	=GRAY_SCALES["10"],
			)-> str					:

		"""
			Produce ascii text of image
		"""

		current = self.ascii_list(source_image_path, columns_number, font_scale, gray_scale_variant)
		self.probe = "\n".join(current)


		return	self.probe




	def average_L(self, source :Image) -> npfloat :

		"""
			Average value of graysacle value for PIL Image object
		"""

		# Converting PIL Image object to a numpy array and get dimensions
		img_array = nparray(source)
		W,H = img_array.shape


		return	npavg(img_array.reshape(W*H))




	def ascii_list(
					self,
					source		:str,
					asciicols	:int,
					asciiscale	:float,
					levels		:str,
				)-> list		:

		"""
			Convert "source" absolute path image to the "levels" grayscale list
		"""

		ascii_output = list()


		with Image.open(source).convert("L") as I:

			w,h = I.size
			W = w /asciicols
			H = W /asciiscale
			asciirows = int(h /H)


			if	asciicols >w or asciirows >h: raise ValueError("Small image!")
			for y in range(asciirows):

				# Start of the current ascii line
				ascii_output.append(str())


				Y1 = int(y *H)
				Y2 = h if y == asciirows -1 else int((y +1) *H)


				for x in range(asciicols):

					X1 = int(x *W)
					X2 = w if x == asciicols -1 else int((x +1) *W)


					current_tile = I.crop(( X1,Y1, X2,Y2, ))
					current_gray = int(self.average_L(current_tile))


					current_scale = int((current_gray *(len(levels) -1)) /255)
					ascii_output[y] += levels[current_scale]


		return	ascii_output
















if __name__ == "__main__":

	arguments = ArgumentParser(
		description=str(
			"Convert an image to an ASCII."
			"The result will be displayed to stdout and question about save it or not"
			"will be prompted."
			"To save, absoulte or relative file path must be provided."
			"To ignore the result, empty string must be provided (Enter hit)."
		)
	)
	arguments.add_argument(
		"source",
		help="source image file path (absoulte or relative for current directory)",
	)
	arguments.add_argument(
		"-l", "--levels",
		dest="levels", nargs="?", default="10",
		help="gray scale length (default 10 symbols not inverted)",
	)
	arguments.add_argument(
		"-S", "--scale",
		dest="scale", nargs="?", default=.43,
		help="font scale (default .43 for courier)",
	)
	arguments.add_argument(
		"-c", "--columns",
		dest="columns", nargs="?", default=110,
		help="number of output ASCII columns (default 110 for fullHD split screen)",
	)


	converter = ARTASCII()
	args = arguments.parse_args()


	current_source	= args.source
	current_columns	= int(args.columns)
	currenst_scale	= float(args.scale)
	current_levels	= GRAY_SCALES[args.levels]




	while True:

		print(
			converter.to_text(
				current_source, current_columns, currenst_scale, current_levels,
			)
		)


		action = input(
			str(
				"save - save as file\n"
				"levels - change gray scale\n"
				"scale - change font ratio (vertical scale)\n"
				"columns - change number of columns (horizontal scale)\n"
				"source - convert another image\n"
				"press Enter to exit\n"
			)
		)


		match action:

			case "save":
				if target := input("save as: "):

					converter.save_probe(target)
					break


			case "levels":

				if target := input("new levels (10, 10_I, 20, 20_I, 70, 70_I): "):

					current_levels = GRAY_SCALES[target]
					continue

				break


			case "scale":

				if target := input("new scale (default 0.43): "):

					current_scale = float(target)
					continue

				break


			case "columns":

				if target := input("new number of columns (default 110): "):

					current_columns = int(target)
					continue

				break


			case "source":

				if target := input(f"new source (current \"{current_source}\"): "):

					current_source = target
					continue

				break


			case _: break







