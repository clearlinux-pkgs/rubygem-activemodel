#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-activemodel
Version  : 4.2.3
Release  : 6
URL      : https://rubygems.org/downloads/activemodel-4.2.3.gem
Source0  : https://rubygems.org/downloads/activemodel-4.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
= Active Model -- model interfaces for Rails
Active Model provides a known set of interfaces for usage in model classes.
They allow for Action Pack helpers to interact with non-Active Record models,
for example. Active Model also helps with building custom ORMs for use outside of
the Rails framework.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n activemodel-4.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-activemodel.gemspec

%build
gem build rubygem-activemodel.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
activemodel-4.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/activemodel-4.2.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/AttributeMethodMatcher/cdesc-AttributeMethodMatcher.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/alias_attribute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/attribute_alias%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/attribute_alias-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/attribute_method_affix-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/attribute_method_prefix-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/attribute_method_suffix-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/define_attribute_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/define_attribute_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/ClassMethods/undefine_attribute_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/attribute_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/cdesc-AttributeMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/match_attribute_method%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/method_missing-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/missing_attribute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/respond_to%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/AttributeMethods/respond_to_without_attributes%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/BlockValidator/cdesc-BlockValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Callbacks/cdesc-Callbacks.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Callbacks/define_model_callbacks-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/cdesc-Conversion.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/to_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/to_model-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/to_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Conversion/to_partial_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/attribute_change-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/attribute_changed_by_setter%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/attribute_will_change%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/attributes_changed_by_setter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/cdesc-Dirty.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changed%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changed_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changes_applied-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/changes_include%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/clear_attribute_changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/clear_changes_information-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/previous_changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/reset_attribute%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/reset_changes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/restore_attribute%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/restore_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Dirty/set_attribute_was-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/EachValidator/cdesc-EachValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/add-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/add_on_blank-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/add_on_empty-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/added%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/as_json-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/blank%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/cdesc-Errors.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/clear-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/count-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/delete-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/empty%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/full_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/full_messages-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/full_messages_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/generate_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/get-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/has_key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/include%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/keys-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/messages-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/normalize_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/set-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/to_a-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/to_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/to_xml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Errors/values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/ForbiddenAttributesError/cdesc-ForbiddenAttributesError.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/ForbiddenAttributesProtection/cdesc-ForbiddenAttributesProtection.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/assert_boolean-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/cdesc-Tests.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/model-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_errors_aref-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_model_naming-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_persisted%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_to_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_to_param-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/Tests/test_to_partial_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Lint/cdesc-Lint.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/MissingAttributeError/cdesc-MissingAttributeError.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Model/cdesc-Model.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Model/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Model/persisted%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/%21%7e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/%3c%3d%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/%3d%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/%3d%7e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/_singularize-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/cache_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/cdesc-Name.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/collection-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/element-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/eql%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/human-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/i18n_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/param_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/plural-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/route_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/singular-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/singular_route_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Name/to_str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/cdesc-Naming.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/model_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/param_key-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/plural-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/route_key-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/singular-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/singular_route_key-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Naming/uncountable%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Railtie/cdesc-Railtie.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/ClassMethods/has_secure_password-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/InstanceMethodsOnActivation/authenticate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/InstanceMethodsOnActivation/cdesc-InstanceMethodsOnActivation.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/InstanceMethodsOnActivation/password%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/InstanceMethodsOnActivation/password-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/InstanceMethodsOnActivation/password_confirmation%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/SecurePassword/cdesc-SecurePassword.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serialization/cdesc-Serialization.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serialization/serializable_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/JSON/as_json-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/JSON/cdesc-JSON.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/JSON/from_json-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/Serializer/Attribute/cdesc-Attribute.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/Serializer/MethodAttribute/cdesc-MethodAttribute.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/Serializer/cdesc-Serializer.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/cdesc-Xml.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/from_xml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/Xml/to_xml-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Serializers/cdesc-Serializers.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/StrictValidationFailed/cdesc-StrictValidationFailed.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/TestCase/cdesc-TestCase.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Translation/cdesc-Translation.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Translation/human_attribute_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Translation/i18n_scope-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Translation/lookup_ancestors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/VERSION/cdesc-VERSION.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/AbsenceValidator/cdesc-AbsenceValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/AcceptanceValidator/cdesc-AcceptanceValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/Callbacks/ClassMethods/after_validation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/Callbacks/ClassMethods/before_validation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/Callbacks/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/Callbacks/cdesc-Callbacks.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/attribute_method%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/clear_validators%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validates%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validates-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validates_each-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validates_with-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validators-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ClassMethods/validators_on-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/Clusivity/cdesc-Clusivity.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ConfirmationValidator/cdesc-ConfirmationValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/ExclusionValidator/cdesc-ExclusionValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/FormatValidator/cdesc-FormatValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/_merge_attributes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/cdesc-HelperMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_absence_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_acceptance_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_confirmation_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_exclusion_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_format_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_inclusion_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_length_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_numericality_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_presence_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/HelperMethods/validates_size_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/InclusionValidator/cdesc-InclusionValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/LengthValidator/cdesc-LengthValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/NumericalityValidator/cdesc-NumericalityValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/PresenceValidator/cdesc-PresenceValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/WithValidator/cdesc-WithValidator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/cdesc-Validations.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/invalid%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/valid%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validations/validates_with-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/cdesc-Validator.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/kind-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/kind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/Validator/validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/cdesc-ActiveModel.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/eager_load%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/gem_version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/ActiveModel/version-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/activemodel-4.2.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/attribute_methods.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/callbacks.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/conversion.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/dirty.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/errors.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/forbidden_attributes_protection.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/gem_version.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/lint.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/locale/en.yml
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/model.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/naming.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/railtie.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/secure_password.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/serialization.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/serializers/json.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/serializers/xml.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/test_case.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/translation.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/absence.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/acceptance.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/callbacks.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/clusivity.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/confirmation.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/exclusion.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/format.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/inclusion.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/length.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/numericality.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/presence.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/validates.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validations/with.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/validator.rb
/usr/lib64/ruby/gems/2.2.0/gems/activemodel-4.2.3/lib/active_model/version.rb
/usr/lib64/ruby/gems/2.2.0/specifications/activemodel-4.2.3.gemspec
