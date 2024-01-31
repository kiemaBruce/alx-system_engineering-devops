#!/usr/bin/env ruby
if ARGV.length > 0
#	matches = ARGV[0].scan(/from:(?:(\+?\d{11})|(\w+))\].*to/)
	matches = ARGV[0].scan(/from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:([-:\d]+)\]/)
	result = matches.map { |match| match.compact.join(',') }.join(',')
	puts result
end
