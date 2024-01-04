#!/usr/bin/env ruby
if ARGV.length > 0
	str = ""
	result = ARGV[0].match(/from:([+\w\d]+)\].+to:([+\w\d]+)\].+flags:([-\d:]+)\]/)
	index = 0
	while index <= result.size
		if index > 1 && index != (result.size)
			str += ","
		end
		if index > 0
			if result[index] != nil
				str += result[index]
			end
		end
		index += 1
	end
	puts str
end
