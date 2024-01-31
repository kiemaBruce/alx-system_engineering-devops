#!/usr/bin/env ruby
if ARGV.length > 0
	puts ARGV[0].scan(/h.{1}n/).join
end
