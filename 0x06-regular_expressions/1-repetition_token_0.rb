#!/usr/bin/env ruby
if ARGV.length > 0
	str = ""
	matches = ARGV[0].scan(/hbt{2,5}n/)
	for match in matches
		str += match
	end
	puts str
end
