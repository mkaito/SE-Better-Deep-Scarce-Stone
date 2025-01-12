require "spec_helper"
require "factories/generator"

describe "Genconfig::Generator" do
  subject { Genconfig::Generator.new }

  describe "config validator" do
    it "should allow accessing the raw config" do
      config = Factories::Generator.valid_config
      subject.config = config
      _(subject.config).must_equal config
    end
  end
end
