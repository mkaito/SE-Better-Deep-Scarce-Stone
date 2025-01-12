require "spec_helper"

describe "TestProfile" do
  subject { Genconfig::Profile.new }
  it "Worky work" do
    _(subject).wont_be_nil
  end
end
