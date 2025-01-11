require "test_helper"

class TestGenconfig < Minitest::Test
  def test_that_it_has_a_version_number
    refute_nil ::Genconfig::VERSION
  end
end
