require_relative "genconfig/version"
require_relative "genconfig/profile"

module Genconfig
  class Error < StandardError; end

  class Generator
    attr_accessor :config

    def valid?
      @config.has_key?(:ore_templates) && @config.has_key?(:planets)
    end
  end
end
