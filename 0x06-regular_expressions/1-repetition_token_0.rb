#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	match_arr = capt.scan(/hbt{2,5}n/m)
	if match_arr.length > 0
		r_str = match_arr.join("\n")
		puts r_str
	else
		exit
	end
else
	exit
end
