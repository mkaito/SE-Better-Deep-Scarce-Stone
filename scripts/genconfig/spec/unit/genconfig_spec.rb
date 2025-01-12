require "spec_helper"
require "factories/generator"

describe "Genconfig::Generator" do
  subject { Genconfig::Generator.new }

  it "should exist" do
    _(subject).wont_be_nil
  end

  describe "valid?" do
    it "should be valid with valid config" do
      subject.config = Factories::Generator.valid_config
      _(subject).must_be :valid?
    end

    it "should be invalid without ore_templates" do
      config = Factories::Generator.valid_config
      config.delete(:ore_templates)
      subject.config = config
      _(subject).wont_be :valid?
    end

    it "should be invalid without planets" do
      config = Factories::Generator.valid_config
      config.delete(:planets)
      subject.config = config
      _(subject).wont_be :valid?
    end
  end
end
