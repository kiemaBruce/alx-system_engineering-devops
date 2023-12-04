#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	matched_arr = capt.scan(/(School)/)
	if matched_arr
		r_str = matched_arr.join('')
		puts r_str
	end
else
	exit
end
