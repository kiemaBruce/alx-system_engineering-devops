#!/usr/bin/env ruby
if !ARGV.empty?
	capt = ARGV[0]
	match_data = capt.match(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:((\W|\d)+)\]/)
	if match_data
		sender = match_data[1]
		receiver = match_data[2]
		flags = match_data[3]
		r_str = [sender, receiver, flags].join(',')
		puts r_str
	else
		exit
	end
else
	exit
end
