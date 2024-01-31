#!/usr/bin/env ruby
if ARGV.length > 0
	puts ARGV[0].scan(/^\d{10}$/).join
end
