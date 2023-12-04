#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	match_arr = capt.scan(/^(\d{3})(\d{3})(\d{4})$/)
	r_str = match_arr.join('')
	puts r_str
else
	exit
end
