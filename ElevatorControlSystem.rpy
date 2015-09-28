I-Logix-RPY-Archive version 8.11.0 C++ 9499822
{ IProject 
	- _id = GUID 58973ca0-f5f7-4c37-a09f-0d4e05280622;
	- _myState = 8192;
	- _name = "ElevatorControlSystem";
	- _modifiedTimeWeak = 9.28.2015::10:12:57;
	- _lastID = 2;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID 7888e5a7-3deb-4e9a-aa52-542a3bdcede8;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID a30fbc67-dfef-4ec4-adfb-2016afd5a08e;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 6;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "5";
			- _count = 7;
		}
		{ IMultiplicityItem 
			- _name = "2";
			- _count = 9;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 7888e5a7-3deb-4e9a-aa52-542a3bdcede8;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID d77efad2-b544-4653-97b7-40fea42b9e6e;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "ElevatorModel";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "9.28.2015::7:57:11";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 0f36c393-ab41-4280-8493-00604af0697b;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID d77efad2-b544-4653-97b7-40fea42b9e6e;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 4;
				{ CGIClass 
					- _id = GUID 641af7bd-77fd-4cf6-bb68-6d4141cd6bd7;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 3a07a030-376c-40b2-9eae-e80dfb87bd25;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID eb90621e-a404-4300-99d4-2f2543509ca3;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID c36f4eb8-2131-414d-9fd7-fb377649086c;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID d26cc330-e0dc-46e2-a095-6f337b6fc475;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "SystemController";
						- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
					}
					- m_pParent = GUID 641af7bd-77fd-4cf6-bb68-6d4141cd6bd7;
					- m_name = { CGIText 
						- m_str = "SystemController";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.11237 0 0 0.101604 104.775 9.5722 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID b9091d32-59a3-45ce-ad07-95c3f1ac8aac;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID e1e481ca-98fe-46fe-96b8-67067aac8aa6;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID ff37bf15-69ba-42e2-b0d9-d68f31a87b6f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Floor";
						- _id = GUID 1fd8a700-e7f5-42ab-8b56-3291f115e3cc;
					}
					- m_pParent = GUID 641af7bd-77fd-4cf6-bb68-6d4141cd6bd7;
					- m_name = { CGIText 
						- m_str = "Floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.13881 0 0 0.101604 350.722 12.5722 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 8a776390-a2fb-4771-a373-1282365f72c3;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 6cc56d9e-aa71-430b-83f4-d6542d850cd4;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID ee560559-22d7-463a-9e06-5879ff1ab64a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Elevator";
						- _id = GUID e2d4b5e4-957c-4e08-9817-ef7a4ec4e4c9;
					}
					- m_pParent = GUID 641af7bd-77fd-4cf6-bb68-6d4141cd6bd7;
					- m_name = { CGIText 
						- m_str = "Elevator";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.151086 0 0 0.101604 97.6978 239.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 60e4f304-4acb-405c-96c9-9a8739bf0df7;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 33da65ea-5738-4074-b8f0-b7df1815e8e6;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 641af7bd-77fd-4cf6-bb68-6d4141cd6bd7;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 7888e5a7-3deb-4e9a-aa52-542a3bdcede8;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID a30fbc67-dfef-4ec4-adfb-2016afd5a08e;
		}
	}
	- PanelDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IPanelDiagram 
			- _id = GUID 24d6188f-ca67-4efe-8853-eed84c4b6d25;
			- _myState = 10240;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PushButton";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,50";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "paneldiagram_1";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "9.28.2015::10:13:5";
			- _graphicChart = { CGIClassChart 
				- _id = GUID e95888d5-cc26-40e9-8371-2807cd053e96;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IPanelDiagram";
					- _id = GUID 24d6188f-ca67-4efe-8853-eed84c4b6d25;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 76;
				{ CGIBox 
					- _id = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_type = 215;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Default.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Default";
						- _id = GUID 7888e5a7-3deb-4e9a-aa52-542a3bdcede8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIActiveX 
					- _id = GUID 6cc9550f-92bc-449f-9c1c-054276f4d945;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "Name";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "doorOpen";
						- _id = GUID 5ca1f6f2-a5e2-42dc-ab93-9bcfc438a4e3;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "dooropen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 47 122.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].doorOpen";
					- m_csName = "dooropen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d8d922b2-7cf1-41c3-a39e-7d6586a20a82;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "doorOpen";
						- _id = GUID 5ca1f6f2-a5e2-42dc-ab93-9bcfc438a4e3;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "dooropen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 50 382.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].doorOpen";
					- m_csName = "dooropen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID f744f306-6805-46be-8e43-b8466c9895d0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "currentLevel";
						- _id = GUID 875746b4-88d6-4fc9-9ee9-1b4d172eeb9c;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00116527 0 0 0.00139443 117 70.5533 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].currentLevel";
					- m_csName = "floor";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 2d71b217-cf5e-4991-82b0-4a92700c69f5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "currentLevel";
						- _id = GUID 875746b4-88d6-4fc9-9ee9-1b4d172eeb9c;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "floor";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00116527 0 0 0.00139443 120 319.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].currentLevel";
					- m_csName = "floor";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 3eed0567-733a-488a-8f28-b2d9da700cf4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.direction.up";
						- _id = GUID 859784fa-f56a-4c24-80c4-705c69051069;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 110 30.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.up";
					- m_csName = "led_2";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID cb2944e1-5c51-47b1-b522-7055734df066;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.direction.down";
						- _id = GUID a339bf6b-04d8-4c65-8e5c-2be9d9bda05a;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 240 30.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.down";
					- m_csName = "led_3";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 98b05288-04bb-450f-adb6-176269f6c603;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.direction.up";
						- _id = GUID 859784fa-f56a-4c24-80c4-705c69051069;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 113 284.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.up";
					- m_csName = "led_4";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID eecabb2e-5aef-4499-a7e7-c2ecc1c920ca;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.direction.down";
						- _id = GUID a339bf6b-04d8-4c65-8e5c-2be9d9bda05a;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 233 284.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.down";
					- m_csName = "led_5";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 6816162f-38c2-4027-9232-c23129505ab0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "currentLevel";
						- _id = GUID 875746b4-88d6-4fc9-9ee9-1b4d172eeb9c;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.00046611 0 0 0.000278887 163 9.31067 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].currentLevel";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 825ddbcc-8c26-460b-849b-6b47f5bef145;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "currentLevel";
						- _id = GUID 875746b4-88d6-4fc9-9ee9-1b4d172eeb9c;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000572927 0 0 0.000278887 156 260.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].currentLevel";
					- m_csName = "digitaldisplay_1";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 2a849397-a262-4d03-82ec-4e8330ca1f33;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 309 196.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[0].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "G";
				}
				{ CGIMFCCtrl 
					- _id = GUID 871c9440-03c4-46a6-b4c7-f1012b20d7d5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 309 161.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[1].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "2";
				}
				{ CGIMFCCtrl 
					- _id = GUID e9510e37-50f6-4f4f-aa82-ea731b7ed0ea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 308 124.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[2].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "3";
				}
				{ CGIMFCCtrl 
					- _id = GUID b90d3f42-10f7-4778-a416-61e6b9fe8963;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 310 88.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[3].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "4";
				}
				{ CGIMFCCtrl 
					- _id = GUID d0e5adc8-3b1c-4188-83c1-9fbd38fc0205;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 311 48.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[4].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "5";
				}
				{ CGIActiveX 
					- _id = GUID 06e0cfe8-9a43-42a1-9d66-cc9278aa7081;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 377 62.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[4].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 9dc3dcaa-0c00-46dd-98db-956688e559b3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 376 101.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[3].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID da793f7c-1385-4200-ba6f-d648cdf7dcc7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 377 139.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[2].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID c4baa6e1-eb46-4bd1-928e-f620efc26514;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 376 178.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[1].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 7e9b90f3-a6a5-4528-a900-40c0fcc66ad4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 376 211.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[0].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 2c25ac44-d357-49ac-929e-79e46d20ab9b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 302 455.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[0].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "G";
				}
				{ CGIMFCCtrl 
					- _id = GUID b9010e01-7938-464f-95ac-25961d4cf656;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 301 407.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[1].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "2";
				}
				{ CGIMFCCtrl 
					- _id = GUID f44fa98b-ba77-4a27-80d8-e44b70c5b21f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 301 363.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[2].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "3";
				}
				{ CGIMFCCtrl 
					- _id = GUID 490a8606-46f7-481a-8db2-0d0c192ec983;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 300 318.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[3].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "4";
				}
				{ CGIMFCCtrl 
					- _id = GUID a6b65493-c80e-42e7-8193-10c191020fc1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "evLevelButtonOn()";
						- _id = GUID 0a8337e4-76e6-477d-a939-228fc3972ebd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000485531 0 0 0.000278887 299 280.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[4].evLevelButtonOn";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "5";
				}
				{ CGIActiveX 
					- _id = GUID b6af3e72-dcfc-416d-b735-da410ac228bf;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 370 291.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[4].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID a7126fb6-2fa6-4bd8-9206-e4a8b2e9b993;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 369 331.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[3].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 6cfe8743-c6bc-429c-b1af-7bf9ab66a82b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 370 378.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[2].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 272375b6-14b8-472e-92d1-10b2870eb6b3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 371 418.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[1].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 771305f0-aa01-4840-9ee7-f07f9f3dbf41;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "LevelButton";
						- _name = "on";
						- _id = GUID 11a20cf4-14f2-4501-862d-da40e852db6e;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000126238 0 0 0.000113298 374 461.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[0].on";
					- m_csName = "led_6";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 86dc6860-c358-4ee7-9aab-f2fac4f23574;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 2b817631-9422-4f5d-a47a-4d380611d47f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evOpen()";
						- _id = GUID f85d2bd6-333d-4b94-b0b8-68fe3d2aa7d7;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000708876 0 0 0.000348608 437 38.3884 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evOpen";
					- m_csName = "pushbutton_10";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "<<|>>";
				}
				{ CGIMFCCtrl 
					- _id = GUID 6b7cba8b-13c1-4491-9c87-d5cb5aab218c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evClose()";
						- _id = GUID bcc95ae7-65b3-453e-b25f-2ae18049511d;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000718586 0 0 0.000366039 436 89.4078 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evClose";
					- m_csName = "pushbutton_11";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = ">>|<<";
				}
				{ CGIMFCCtrl 
					- _id = GUID b60b7958-6322-4c14-9d98-a5408d35f19b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evAlarm()";
						- _id = GUID bbcee87b-0518-49e6-bd85-8c0aaeb71e85;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000747718 0 0 0.000296317 432 154.33 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evAlarm";
					- m_csName = "pushbutton_12";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Alarm";
				}
				{ CGIMFCCtrl 
					- _id = GUID 0441d1ca-b56c-47de-a764-246763a41a9f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evStop()";
						- _id = GUID c49c7215-b419-40cf-b8dd-7806da8573dd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.00077685 0 0 0.000261456 428 203.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evStop";
					- m_csName = "pushbutton_13";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Stop";
				}
				{ CGIActiveX 
					- _id = GUID d78c7be2-ae1d-4084-b353-6e1ae8fc4e29;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.alarm.activated";
						- _id = GUID 18ff7189-edc8-4d58-b6c7-7023f6abdd38;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "activated";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 547 176.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.activated";
					- m_csName = "led_16";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 182804fc-2511-4c9c-9766-ee07c7021bae;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.state_5.stopped";
						- _id = GUID cfa05e62-52c9-4a89-9741-fe3b46283220;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "stopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 546 220.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.stopped";
					- m_csName = "led_17";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 99247812-3be9-4864-954b-69b8b720a3cb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evOpen()";
						- _id = GUID f85d2bd6-333d-4b94-b0b8-68fe3d2aa7d7;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000708876 0 0 0.000348608 427 276.388 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evOpen";
					- m_csName = "pushbutton_10";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "<<|>>";
				}
				{ CGIMFCCtrl 
					- _id = GUID 81e25770-4637-4dcd-bc9a-1a9888c77fee;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evClose()";
						- _id = GUID bcc95ae7-65b3-453e-b25f-2ae18049511d;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000718586 0 0 0.000366039 428 333.408 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evClose";
					- m_csName = "pushbutton_11";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = ">>|<<";
				}
				{ CGIMFCCtrl 
					- _id = GUID c1778157-5f18-44b3-ac5b-a894b6fca2ad;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evAlarm()";
						- _id = GUID bbcee87b-0518-49e6-bd85-8c0aaeb71e85;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000747718 0 0 0.000296317 427 397.33 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evAlarm";
					- m_csName = "pushbutton_12";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Alarm";
				}
				{ CGIMFCCtrl 
					- _id = GUID 63eed424-e6e2-4720-b313-8d670daa3aea;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evStop()";
						- _id = GUID c49c7215-b419-40cf-b8dd-7806da8573dd;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.00077685 0 0 0.000261456 428 456.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evStop";
					- m_csName = "pushbutton_13";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Stop";
				}
				{ CGIActiveX 
					- _id = GUID c8f95798-ba5c-4964-b564-5fff7b0b26d1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.alarm.activated";
						- _id = GUID 18ff7189-edc8-4d58-b6c7-7023f6abdd38;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "activated";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 553 413.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.activated";
					- m_csName = "led_16";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 11b01ead-3b74-4103-ba90-12a1140628e7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.state_5.stopped";
						- _id = GUID cfa05e62-52c9-4a89-9741-fe3b46283220;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "stopped";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 551 464.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.stopped";
					- m_csName = "led_17";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 48ca6483-c5cb-4a05-a723-5517842d6a30;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evRegular()";
						- _id = GUID ca4cbef9-0aac-4640-aaab-d651a67b33a9;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000708876 0 0 0.000322463 641 19.3592 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evRegular";
					- m_csName = "pushbutton_18";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Regular";
				}
				{ CGIMFCCtrl 
					- _id = GUID 17da857c-3164-4824-8e14-a39a03284120;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evFreight()";
						- _id = GUID 234e7117-c603-41af-9604-04daed827933;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000738007 0 0 0.000322463 745 18.3592 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evFreight";
					- m_csName = "pushbutton_19";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Freight";
				}
				{ CGIMFCCtrl 
					- _id = GUID ce7279b9-f49c-428f-876f-e4890dd0db33;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evMaintenance()";
						- _id = GUID 8fe0e0ad-ef2a-4c27-8497-2a6db6254540;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000825403 0 0 0.000366038 850 18.4078 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evMaintenance";
					- m_csName = "pushbutton_19";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Maintenance";
				}
				{ CGIActiveX 
					- _id = GUID a0481343-a0f6-44b2-968f-b71959a92f17;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.regular";
						- _id = GUID 55c54c60-dff2-42a7-9b6f-ea321ca7bb35;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "regular";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 669 81.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.regular";
					- m_csName = "led_20";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID e1c96f88-fa42-48d4-86ec-db8b61354e33;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.freight";
						- _id = GUID 8a81982a-779b-4313-9fbd-dcf2cc4ff7bb;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "freight";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 783 80.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.freight";
					- m_csName = "led_21";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 583eb26c-3ba5-40af-9233-a57e68a0dc43;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.maintenance";
						- _id = GUID bcf2e125-90d1-423b-9145-ecf61e9145f7;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "maintenance";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 886 82.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_21.maintenance";
					- m_csName = "led_22";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID d287733e-0f0e-4905-990c-8e4a7e40362a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evRegular()";
						- _id = GUID ca4cbef9-0aac-4640-aaab-d651a67b33a9;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000708876 0 0 0.000322463 635 437.359 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evRegular";
					- m_csName = "pushbutton_18";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Regular";
				}
				{ CGIMFCCtrl 
					- _id = GUID 13fc9440-c1d0-4e3b-a75a-85b155f1b874;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evFreight()";
						- _id = GUID 234e7117-c603-41af-9604-04daed827933;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000738007 0 0 0.000322463 744 440.359 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evFreight";
					- m_csName = "pushbutton_19";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Freight";
				}
				{ CGIMFCCtrl 
					- _id = GUID 8f1dc897-b6a8-46df-86c0-91e73f600fcb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "evMaintenance()";
						- _id = GUID 8fe0e0ad-ef2a-4c27-8497-2a6db6254540;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000825403 0 0 0.000366038 843 438.408 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evMaintenance";
					- m_csName = "pushbutton_19";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Maintenance";
				}
				{ CGIActiveX 
					- _id = GUID 21fca3bc-c21d-4363-aa8f-9ad272cd9882;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.regular";
						- _id = GUID 55c54c60-dff2-42a7-9b6f-ea321ca7bb35;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "regular";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 671 421.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.regular";
					- m_csName = "led_20";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d736488c-0477-49f3-b684-667f83ab75e6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.freight";
						- _id = GUID 8a81982a-779b-4313-9fbd-dcf2cc4ff7bb;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "freight";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 780 421.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.freight";
					- m_csName = "led_21";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID da4fe927-876c-4190-869b-9a20636f5f1e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.Active.mode.maintenance";
						- _id = GUID bcf2e125-90d1-423b-9145-ecf61e9145f7;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "maintenance";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 885 422.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_21.maintenance";
					- m_csName = "led_22";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID ec4eca1d-fd04-4501-810e-0b4720c79dd2;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID c1392526-e1e1-485d-9e0d-05f8535a9dd4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evUpButton()";
						- _id = GUID 6eef3d5c-aa18-4c31-9981-2f95917d679f;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 665 346.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[0].evUpButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID ef5e30ca-ff02-4b04-8a11-470ec2bb2e92;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evUpButton()";
						- _id = GUID 6eef3d5c-aa18-4c31-9981-2f95917d679f;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 663 294.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].evUpButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID ca57a12e-0dfd-4092-958c-8b8d2dab5b4a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evUpButton()";
						- _id = GUID 6eef3d5c-aa18-4c31-9981-2f95917d679f;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 662 235.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].evUpButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID 3f388823-9140-498b-882b-45b58ce15c49;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evUpButton()";
						- _id = GUID 6eef3d5c-aa18-4c31-9981-2f95917d679f;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 663 186.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].evUpButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID 0400dd2d-e161-4722-a074-501c311290b4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evDownButton()";
						- _id = GUID a464b827-749c-466f-85b0-fd6e2ae90982;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 759 297.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].evDownButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 79e71e04-cf43-44b8-998f-3f0849c665ca;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evDownButton()";
						- _id = GUID a464b827-749c-466f-85b0-fd6e2ae90982;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 761 237.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].evDownButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 34726086-2ee1-4418-881d-8690c680b22b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evDownButton()";
						- _id = GUID a464b827-749c-466f-85b0-fd6e2ae90982;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 758 182.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].evDownButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 138cf1f1-364a-4c53-b85e-589ea450e827;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "None";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "evDownButton()";
						- _id = GUID a464b827-749c-466f-85b0-fd6e2ae90982;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 8192;
					- m_transform = 0.000602059 0 0 0.000261456 753 130.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].evDownButton";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIActiveX 
					- _id = GUID 1654a900-481a-4ae5-ab22-11756f4b0934;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "up";
						- _id = GUID f82a77fe-fa30-41a9-9547-affd4635bc43;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 613 359.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[0].up";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID b9614eb2-c4a3-44db-b0d1-393b64434d9a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "up";
						- _id = GUID f82a77fe-fa30-41a9-9547-affd4635bc43;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 612 300.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].up";
					- m_csName = "led_27";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d6b08620-0d5c-4c0b-9538-31fb0d03fab2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "up";
						- _id = GUID f82a77fe-fa30-41a9-9547-affd4635bc43;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 612 239.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].up";
					- m_csName = "led_28";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 80217e42-3754-4033-938f-322c87b87033;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "up";
						- _id = GUID f82a77fe-fa30-41a9-9547-affd4635bc43;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 614 187.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].up";
					- m_csName = "led_29";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID de56dad2-0464-4af5-8edb-f863e11afa07;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "down";
						- _id = GUID f1f87feb-bf41-4889-a2fa-8c6b72d7e3ae;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 862 134.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].down";
					- m_csName = "led_30";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 0438daf2-d203-4bdc-8389-a0a3f73c4c0c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "down";
						- _id = GUID f1f87feb-bf41-4889-a2fa-8c6b72d7e3ae;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 862 194.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].down";
					- m_csName = "led_31";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID adbcd0ee-b156-490a-bb3a-1af6c396b878;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "down";
						- _id = GUID f1f87feb-bf41-4889-a2fa-8c6b72d7e3ae;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 865 250.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].down";
					- m_csName = "led_32";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID c9863adc-9481-4d7c-b1da-25ca7292bf8f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "BoundElement";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "down";
						- _id = GUID f1f87feb-bf41-4889-a2fa-8c6b72d7e3ae;
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 2048;
					- m_transform = 0.000126238 0 0 0.000113298 864 314.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].down";
					- m_csName = "led_33";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 70faed5b-161b-40f2-baad-4b0808dfaaa1;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 68e2b1bc-ef93-44a5-9c7a-a03528d51cbd;
						}
					}
				}
				{ CGIFreeText 
					- _id = GUID 0f1c4d37-df17-4dcf-96d3-8f2be2448d1f;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -17 4 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 921 127  970 127  970 145  921 145  ;
					- m_text = "Level 5";
				}
				{ CGIFreeText 
					- _id = GUID 4a50f55b-41c8-47e4-93c3-b020e2e6338d;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -11 1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 918 184  956 184  956 202  918 202  ;
					- m_text = "Level 4";
				}
				{ CGIFreeText 
					- _id = GUID 062fa35e-36bd-4afa-b53a-6e6d71c50522;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -8 1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 916 238  954 238  954 256  916 256  ;
					- m_text = "Level 3";
				}
				{ CGIFreeText 
					- _id = GUID 3096e910-61ed-4aca-ac97-f292c606dd34;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -8 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 914 299  952 299  952 317  914 317  ;
					- m_text = "Level 2";
				}
				{ CGIFreeText 
					- _id = GUID b97c00b7-b51b-4e6f-acda-aad55d7ce56f;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -10 1 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 918 355  968 355  968 373  918 373  ;
					- m_text = "Gournd";
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 5d5af1e6-1c5f-4db1-9d04-2e501a0470d2;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 7888e5a7-3deb-4e9a-aa52-542a3bdcede8;
			}
		}
	}
}

