#!/usr/bin/env ruby
if ARGV.length > 0
	str = ""
	matches = ARGV[0].scan(/^\d{10}$/)
	for match in matches
		str += match
	end
	puts str
end