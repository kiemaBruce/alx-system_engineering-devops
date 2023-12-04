#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	match_arr = capt.scan(/([A-Z])/)
	r_str = match_arr.join('')
	puts r_str
else
	exit
end
