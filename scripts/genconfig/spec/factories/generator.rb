module Factories
  class Generator
    class << self
      def valid_config
        {ore_templates: {}, planets: {}}
      end
    end
  end
end
