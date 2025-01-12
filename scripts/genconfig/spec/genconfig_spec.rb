require "spec_helper"

describe "Genconfig" do
  subject { Genconfig::Generator.new }

  it "must exist" do
    _(subject).wont_be_nil
  end
end
