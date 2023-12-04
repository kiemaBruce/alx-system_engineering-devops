#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	match_arr = capt.scan(/hb?tn/)
	r_str = match_arr.join("\n")
	puts r_str
else
	exit
end
