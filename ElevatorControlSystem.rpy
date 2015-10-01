I-Logix-RPY-Archive version 8.11.0 C++ 9499822
{ IProject 
	- _id = GUID f1c248bf-1144-4a28-86dc-0d9960d32332;
	- _myState = 8192;
	- _name = "ElevatorControlSystem";
	- _modifiedTimeWeak = 10.1.2015::2:17:25;
	- _lastID = 3;
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
		- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 78aef2d2-bd7a-4621-a42a-52d6844b9069;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 7;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 9;
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
			- _count = 11;
		}
		{ IMultiplicityItem 
			- _name = "2";
			- _count = 2;
		}
		{ IMultiplicityItem 
			- _name = "6";
			- _count = 1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre81Cpp";
			- _id = GUID dcd2cdb5-4c74-4d47-99ca-1b358b271e5f;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre812Cpp";
			- _id = GUID 3026d3ea-02b4-49ae-b086-6982c27412f0;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre813Cpp";
			- _id = GUID 803c9619-7509-44c3-bfdf-6fee2352ab55;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 4b55e283-fff5-4a6a-8e1f-5893024b3d66;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Aggregation";
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
							{ IPropertyMetaclass 
								- _Name = "Composition";
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
								- _Name = "Object";
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
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
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
			- _lastModifiedTime = "9.30.2015::5:9:29";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 98be26a6-f7a4-41c2-9b6a-81ea1092b3b2;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 4b55e283-fff5-4a6a-8e1f-5893024b3d66;
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
				- elementList = 6;
				{ CGIClass 
					- _id = GUID b0f146c4-dd11-4370-af6c-12ab794dffe9;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID bce905d6-98b0-4c9d-99a8-09c10b338e03;
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
							- _id = GUID fccb4f96-8182-4c95-8b3b-2e196649c022;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 66da0c0c-8db1-4bec-868f-9ae9b563ea8a;
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
					- _id = GUID eea8c408-0a03-44cd-8fd2-d825bc401a01;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "SystemController";
						- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
					}
					- m_pParent = GUID b0f146c4-dd11-4370-af6c-12ab794dffe9;
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
					- m_transform = 0.128423 0 0 0.101604 281.743 110.572 ;
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
							- _id = GUID de71c1ec-5e85-4621-aa9d-3f26125c6913;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 6ac2901c-2444-45dd-b972-3342458f389e;
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
					- _id = GUID 1ac8def7-070a-48a6-97ca-b9d9c2b5ea27;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
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
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Elevator";
						- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
					}
					- m_pParent = GUID b0f146c4-dd11-4370-af6c-12ab794dffe9;
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
					- m_transform = 0.226629 0 0 0.12656 241.547 326.362 ;
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
							- _id = GUID b26daca3-16a8-4986-a40c-b62847c7a4d6;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 9c22e805-e62f-4356-9454-089d1d071ee6;
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
				{ CGIAssociationEnd 
					- _id = GUID d3639239-78c1-488b-82b8-5b1704cb619c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
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
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "system";
						- _id = GUID 6ee2623c-0242-4883-9539-4c2cde69698c;
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
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 0;
					- m_pSource = GUID 1ac8def7-070a-48a6-97ca-b9d9c2b5ea27;
					- m_sourceType = 'F';
					- m_pTarget = GUID eea8c408-0a03-44cd-8fd2-d825bc401a01;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
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
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 479 384 ;
					- m_TargetPort = 532 890 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID 2f5ac455-8c6e-495f-98b7-ac983050851f;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Floor";
						- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
					}
					- m_pParent = GUID b0f146c4-dd11-4370-af6c-12ab794dffe9;
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
					- m_transform = 0.0793201 0 0 0.101604 617.841 199.572 ;
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
							- _id = GUID 0acc44fb-de5d-4d6a-9e6d-0cf2137b9d8e;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID eb942846-8387-4a92-960c-08f4efe52208;
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
				{ CGIAssociationEnd 
					- _id = GUID 0ba35cc5-d27f-4c98-9c5b-f944ddc5665d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
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
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Floor";
						- _name = "system";
						- _id = GUID a8949e10-4a1c-41eb-aab2-264562356000;
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
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 0;
					- m_pSource = GUID 2f5ac455-8c6e-495f-98b7-ac983050851f;
					- m_sourceType = 'F';
					- m_pTarget = GUID eea8c408-0a03-44cd-8fd2-d825bc401a01;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
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
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 518 290  518 201  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 890 ;
					- m_TargetPort = 531 890 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 7;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID b0f146c4-dd11-4370-af6c-12ab794dffe9;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 78aef2d2-bd7a-4621-a42a-52d6844b9069;
		}
	}
	- PanelDiagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IPanelDiagram 
			- _id = GUID babaa37a-4fe5-4df7-a665-ef528c27e423;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
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
										- _Name = "PanelControlTypeBindingDisplay";
										- _Value = "PredefinedOnly";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,PredefinedOnly";
									}
								}
							}
						}
					}
				}
			}
			- _name = "panel";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "10.1.2015::2:17:28";
			- _graphicChart = { CGIClassChart 
				- _id = GUID bd1708f0-a23c-436a-8518-ab8d6c77ace4;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IPanelDiagram";
					- _id = GUID babaa37a-4fe5-4df7-a665-ef528c27e423;
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
				- elementList = 93;
				{ CGIBox 
					- _id = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
					- m_type = 215;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Default.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Default";
						- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
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
					- _id = GUID 4439da30-b2cc-40c4-ac35-6abcb32560f6;
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
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
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
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "displayLevel";
						- _id = GUID ba1f1bd0-88c6-421d-83f9-f7a53e3fba1b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.00116527 0 0 0.00139443 118 146.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].displayLevel";
					- m_csName = "levelindicator_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID bd3d75a7-d8c7-4a90-b582-c0db57761e45;
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
						- _name = "displayLevel";
						- _id = GUID ba1f1bd0-88c6-421d-83f9-f7a53e3fba1b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000407846 0 0 0.000278887 161 81.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].displayLevel";
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
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 8140128e-693a-48a3-81cf-c966fd7cfaa3;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 748 235.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID cb6d415f-6c4f-4731-ad80-788d2d74b64b;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 746 287.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID c0bf40df-27f9-494a-9ffc-9d120b537ebd;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 746 333.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID d00b923f-daba-42ed-8878-73db8113479b;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 746 415.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[0].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIActiveX 
					- _id = GUID a09183b6-b5c5-44da-9994-a968c5fd60fe;
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 696 240.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 13907376-f8fc-4c9e-824b-da2fb000e6f1;
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 696 293.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 568f3dab-7f1c-4016-92a6-0419ac17a497;
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 696 338.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 70b8d490-a8c3-4886-8274-6d462114b682;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 699 428.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[0].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 6ae90848-9f6e-4fc9-990f-325622461243;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 840 189.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[5].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 52b0cf2e-3cf0-46e2-8242-150cc596f538;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 843 236.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 9a79ba3c-d8ca-4fba-a594-060712d11cd5;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 841 285.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID 1f8bcfb5-c831-4873-8e5b-2c9937978292;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 842 331.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIActiveX 
					- _id = GUID 4cc320ce-be5d-4b6d-8ce3-c5a4b3d10c48;
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 913 196.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[5].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 3047405b-265e-4924-ac24-c2936c73c686;
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 912 244.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[4].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 5d9b7926-556d-4a8a-987e-7b35cc8ded32;
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 912 294.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[3].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID cdf78e80-07bc-44f7-85ff-140399057937;
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 915 342.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[2].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 1a994e8d-af54-414b-ac83-c41a1c451b92;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _id = GUID fdef9928-b6f7-4160-809b-432aaf63cf9f;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
					- m_name = { CGIText 
						- m_str = "door open";
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
					- m_transform = 0.000126238 0 0 0.000113298 70 196.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].doorOpen";
					- m_csName = "door open";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 5794aea1-0f7b-48ad-aad0-c6ff35f568a5;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 311 275.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[0].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "B";
				}
				{ CGIMFCCtrl 
					- _id = GUID 9a63b5db-76ad-4d8e-8fef-79fdcdd39466;
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
						- _id = GUID 7253a803-db22-4647-9a13-5f143b3db28c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 439 141.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evClose";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = ">>|<<";
				}
				{ CGIMFCCtrl 
					- _id = GUID 25dd2dbc-5748-426d-ad6b-ec97a166863f;
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
						- _id = GUID 590591ec-aa3d-4bdb-9ba5-58ff6a90585b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 441 90.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evOpen";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "<<|>>";
				}
				{ CGIFreeText 
					- _id = GUID 2205cdd7-a41c-4978-8ecc-8a6e5b32ad20;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -60 -23 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1099 445  1099 477  1037 477  ;
					- m_text = "Basement";
				}
				{ CGIFreeText 
					- _id = GUID 4cc3d756-c8d4-4ae3-9f29-733036d4782b;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -55 -107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 2";
				}
				{ CGIFreeText 
					- _id = GUID 64943312-ac39-4398-87a9-a2264151feff;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -55 -153 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 3";
				}
				{ CGIFreeText 
					- _id = GUID efca0737-59a1-4c0d-8e55-b3f21c1cdace;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -56 -203 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 4";
				}
				{ CGIFreeText 
					- _id = GUID 2eb9af2e-cec1-43cc-b785-05a794fe9f09;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -56 -251 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 5";
				}
				{ CGIMFCCtrl 
					- _id = GUID c65c83a2-726e-4cc1-b114-65649d7af836;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 312 196.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[2].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "2";
				}
				{ CGIMFCCtrl 
					- _id = GUID c822b3a7-ce40-4717-afa3-ce7e2ea6830a;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 311 154.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[3].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "3";
				}
				{ CGIMFCCtrl 
					- _id = GUID 96014a32-29f4-4cb2-9ba6-0e648185bca8;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 309 116.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[4].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "4";
				}
				{ CGIMFCCtrl 
					- _id = GUID 3eee3619-c76c-44b8-9f59-a0115c715e57;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 310 76.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[5].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "5";
				}
				{ CGIActiveX 
					- _id = GUID 37765dfa-19c0-4689-8f84-35d9fa437ffe;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 378 126.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[4].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID f6b2c99e-c94c-4016-9e5a-73b96232dcbd;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 376 90.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[5].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 7d0de42d-2061-47ea-a8b5-42b18042b3d0;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 379 166.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[3].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID e675bedf-565a-4081-a4dc-1a06bdf28883;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 378 291.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[0].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 0abfeab9-d2ce-4fb1-8424-f227e5f3bdec;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 380 204.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[2].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 37caf979-3433-4ef2-81fa-1edd3954cfdb;
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
						- _id = GUID 8f53ccbd-27ac-4b3b-ae3b-675639e35a80;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 441 191.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evAlarm";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Alarm";
				}
				{ CGIActiveX 
					- _id = GUID 176c3faa-4fe7-4f8b-8e3b-9613ce01660e;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_5.activated";
						- _id = GUID f7366b97-9fd2-4569-8767-9b2ef73b3ad6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 513 505.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.activated";
					- m_csName = "led_14";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 197b19f9-b227-4036-b087-7db2a471c2d2;
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
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
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
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "displayLevel";
						- _id = GUID ba1f1bd0-88c6-421d-83f9-f7a53e3fba1b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.00116527 0 0 0.00139443 117 439.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].displayLevel";
					- m_csName = "levelindicator_1";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 5a32860e-cb6c-4ba7-8293-c5c27fad11ba;
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
						- _name = "displayLevel";
						- _id = GUID ba1f1bd0-88c6-421d-83f9-f7a53e3fba1b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000407846 0 0 0.000278887 160 379.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].displayLevel";
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
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 1e38380c-b279-4c64-b4b0-c9e213a70418;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 313 592.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[0].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "B";
				}
				{ CGIMFCCtrl 
					- _id = GUID 01bef754-bded-47ec-b88b-3610a44fd8fc;
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
						- _id = GUID 7253a803-db22-4647-9a13-5f143b3db28c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 439 443.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evClose";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = ">>|<<";
				}
				{ CGIMFCCtrl 
					- _id = GUID 35519f4a-c67d-4353-9d96-20c00b3d6cd7;
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
						- _id = GUID 590591ec-aa3d-4bdb-9ba5-58ff6a90585b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 441 392.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evOpen";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "<<|>>";
				}
				{ CGIMFCCtrl 
					- _id = GUID e339cb38-0940-48a6-af79-f31be5ee2d55;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 313 506.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[2].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "2";
				}
				{ CGIMFCCtrl 
					- _id = GUID 0eb657f1-fcbc-40ea-b7c1-863120f9e3b1;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 313 466.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[3].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "3";
				}
				{ CGIMFCCtrl 
					- _id = GUID f87610a4-9707-4be6-a2e1-d7f8a764ffaf;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 311 427.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[4].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "4";
				}
				{ CGIMFCCtrl 
					- _id = GUID dd6ba66c-356a-49c5-8420-91055800cc26;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 310 386.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[5].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "5";
				}
				{ CGIActiveX 
					- _id = GUID 5c92d553-5833-4d97-83cb-1c7abfbb2d77;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 377 438.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[4].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 4a736db5-dd4e-49bb-8717-1795cf42160e;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 376 397.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[5].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID ccd0225a-4267-4dbb-8e82-70fd96ee2f4a;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 378 474.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[3].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 753fb45d-58e1-4161-ac6b-24595553bce1;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 376 603.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[0].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 9f1e435f-3522-46c5-a375-700e8be3caa9;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 377 515.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[2].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 2223071e-60bc-4e53-8e4f-1ffdf7b67d55;
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
						- _id = GUID 8f53ccbd-27ac-4b3b-ae3b-675639e35a80;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 441 493.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evAlarm";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Alarm";
				}
				{ CGIActiveX 
					- _id = GUID 8e3231b6-0e84-4760-a851-eba4a79ed7b2;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_5.activated";
						- _id = GUID f7366b97-9fd2-4569-8767-9b2ef73b3ad6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 517 205.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.activated";
					- m_csName = "led_14";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID a0295c5b-abf9-46ee-ab6c-6925c2c3cb94;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _id = GUID fdef9928-b6f7-4160-809b-432aaf63cf9f;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
					- m_name = { CGIText 
						- m_str = "door open";
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
					- m_transform = 0.000126238 0 0 0.000113298 77 493.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].doorOpen";
					- m_csName = "door open";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 6d42d9ba-e861-4bed-8715-e9ccd07c58a3;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_8.up";
						- _id = GUID db11f678-3db5-4c88-acd0-b0a57ef0923e;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 127 91.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.up";
					- m_csName = "up";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 9efca351-bc9f-4b84-8913-236b78996cbe;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_8.down";
						- _id = GUID 3ca3f67b-5949-4ae6-a7cb-9e4cdabfad42;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 216 92.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.down";
					- m_csName = "down";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 9813ed9c-a703-443c-b723-9174ddbeb293;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_8.up";
						- _id = GUID db11f678-3db5-4c88-acd0-b0a57ef0923e;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 130 384.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.up";
					- m_csName = "up";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 79a6cda0-a103-441c-98b0-21014fe56867;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_8.down";
						- _id = GUID 3ca3f67b-5949-4ae6-a7cb-9e4cdabfad42;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 217 385.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.down";
					- m_csName = "down";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID e763b301-1ee8-43e2-8b9d-e60b205e47c4;
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
						- _id = GUID 3d4b4ee4-010f-41af-8bd2-10e95d27c18c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000718586 0 0 0.000278887 713 54.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evRegular";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Regular";
				}
				{ CGIMFCCtrl 
					- _id = GUID 7a8958b6-dc9a-4094-bf3a-55df996a1b3a;
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
						- _id = GUID ac052df3-591a-4cdd-9a71-6ce81c4f221c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000990483 0 0 0.000278887 932 52.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evMaintenance";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Maintenance";
				}
				{ CGIMFCCtrl 
					- _id = GUID d9d4d8f1-3e17-4c50-b196-92725b8b1b2b;
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
						- _id = GUID 4a503790-34d3-49ef-b6ef-580342fff7ea;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000718586 0 0 0.000278887 824 53.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evFreight";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Freight";
				}
				{ CGIActiveX 
					- _id = GUID 43e763a9-47b5-46ac-a9cf-18d913d6e791;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.regular";
						- _id = GUID 3b06ae75-e329-461f-ace6-862391133fe3;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 745 108.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.regular";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 99850ea2-19d3-442f-96f1-fe9f70515ff5;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.freight";
						- _id = GUID 36b8ae4e-a260-422d-a86d-4eb275c9b6ca;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 853 109.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.freight";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID cd76ab14-2185-4d2d-84b2-2c08f2606351;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.maintenance";
						- _id = GUID 7442c1e7-fd13-43fc-b167-c7654026cd6f;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 973 108.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.maintenance";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID fa10a4d2-32e6-4488-a2a2-0fd628f57803;
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
						- _id = GUID 3d4b4ee4-010f-41af-8bd2-10e95d27c18c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000718586 0 0 0.000278887 720 515.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evRegular";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Regular";
				}
				{ CGIMFCCtrl 
					- _id = GUID 5ecbbc16-71a5-4e45-bd08-fb24ed5abe2b;
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
						- _id = GUID ac052df3-591a-4cdd-9a71-6ce81c4f221c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000990483 0 0 0.000278887 946 515.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evMaintenance";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Maintenance";
				}
				{ CGIMFCCtrl 
					- _id = GUID 84f0c4cb-5e3e-4287-ae8d-33f0b33c7a79;
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
						- _id = GUID 4a503790-34d3-49ef-b6ef-580342fff7ea;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000718586 0 0 0.000278887 836 515.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evFreight";
					- m_csName = "pushbutton_24";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Freight";
				}
				{ CGIActiveX 
					- _id = GUID 9b34a991-c9d7-411c-9909-da40c2796f9c;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.regular";
						- _id = GUID 3b06ae75-e329-461f-ace6-862391133fe3;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 753 568.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.regular";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 5d999adb-88c6-4b20-ba6c-694ace96fb6a;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.freight";
						- _id = GUID 36b8ae4e-a260-422d-a86d-4eb275c9b6ca;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 864 566.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.freight";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 24434c3f-adcb-41de-8889-5e95e65924cb;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_12.maintenance";
						- _id = GUID 7442c1e7-fd13-43fc-b167-c7654026cd6f;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 991 564.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.maintenance";
					- m_csName = "led_26";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 99478213-2774-48e7-a4e8-33a454c4db1b;
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
						- _id = GUID 0d9378ae-d4cf-4b8c-9681-8e73aa016328;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 443 242.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evStop";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Stop";
				}
				{ CGIMFCCtrl 
					- _id = GUID 7a9520fa-a15a-45f3-9a12-bd760cbc401b;
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
						- _id = GUID 0d9378ae-d4cf-4b8c-9681-8e73aa016328;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 440 545.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evStop";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Stop";
				}
				{ CGIActiveX 
					- _id = GUID cb16eddf-87fb-41bc-86e6-9b40c69a4762;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_16.stopped";
						- _id = GUID aed6089a-fed2-4a90-9eb9-b86ac0e3a50c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 517 253.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].statechart_10.stopped";
					- m_csName = "led_14";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID dd0b37cb-699d-42ee-8f70-30d1be91cae1;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "IState";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "ROOT.active.state_16.stopped";
						- _id = GUID aed6089a-fed2-4a90-9eb9-b86ac0e3a50c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 515 555.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].statechart_10.stopped";
					- m_csName = "led_14";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 3db98e2f-3863-443b-b5c6-42ca9f14228b;
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
						- _name = "evLoad()";
						- _id = GUID c63876cc-5591-4c60-8dbc-7fd774c459fa;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 544 91.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evLoad";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Load";
				}
				{ CGIMFCCtrl 
					- _id = GUID 9e895696-b98e-4877-b69d-e26cbd368689;
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
						- _name = "evUnLoad()";
						- _id = GUID 8196cdaa-a67c-47c4-b164-33508ef39192;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 543 150.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].evUnLoad";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "unLoad";
				}
				{ CGIActiveX 
					- _id = GUID d07ff382-fafa-41b7-ad6a-d4a1bfd03662;
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
						- _name = "currLoad";
						- _id = GUID 2c6b035b-e627-494d-9ea1-b661b951bd06;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000738007 0 0 0.000278887 545 34.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].currLoad";
					- m_csName = "digitaldisplay_2";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 946573f5-52e1-44c9-bbce-7b39f20da74b;
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
						- _name = "overLoaded";
						- _id = GUID b9c32e0a-3149-44f2-b6b9-050f5f0b3c2b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
					- m_name = { CGIText 
						- m_str = "over load";
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
					- m_transform = 0.000126238 0 0 0.000113298 466 44.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].overLoaded";
					- m_csName = "over load";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID ae29bc95-2ff6-4b41-8d32-ef5f3f09a7ba;
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
						- _name = "evLoad()";
						- _id = GUID c63876cc-5591-4c60-8dbc-7fd774c459fa;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 535 393.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evLoad";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Load";
				}
				{ CGIMFCCtrl 
					- _id = GUID fd681d21-778d-48f2-869b-1ca31108a93e;
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
						- _name = "evUnLoad()";
						- _id = GUID 8196cdaa-a67c-47c4-b164-33508ef39192;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000582637 0 0 0.000313747 534 444.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].evUnLoad";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "unLoad";
				}
				{ CGIActiveX 
					- _id = GUID 1a484e28-4e0b-4006-9c3c-7ab1f6b08b40;
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
						- _name = "currLoad";
						- _id = GUID 2c6b035b-e627-494d-9ea1-b661b951bd06;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000738007 0 0 0.000278887 537 350.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].currLoad";
					- m_csName = "digitaldisplay_2";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 7609d21c-b740-4dea-8833-294fdea5cee9;
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
						- _name = "overLoaded";
						- _id = GUID b9c32e0a-3149-44f2-b6b9-050f5f0b3c2b;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
					- m_name = { CGIText 
						- m_str = "over load";
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
					- m_transform = 0.000126238 0 0 0.000113298 472 363.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].overLoaded";
					- m_csName = "over load";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 19988110-30a8-4977-bee6-26d9495f9238;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 312 236.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[1].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "G";
				}
				{ CGIActiveX 
					- _id = GUID c927fd4c-90b4-4058-81ba-fe8d32830999;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 381 250.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[0].itsLevel[1].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 91d46825-a298-4c84-9763-636f8aea8629;
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
						- _id = GUID 16c85312-c57f-42d0-9331-ef0296150a20;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000427267 0 0 0.000287602 314 552.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[1].evLevelButtonOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "G";
				}
				{ CGIActiveX 
					- _id = GUID 2ba33720-d129-4854-91c4-46db51a4588b;
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
						- _id = GUID 67db8416-7188-4772-98c5-15e83077d269;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 377 560.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsElevator[1].itsLevel[1].on";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "Elevator";
							- _name = "itsLevel";
							- _id = GUID 7a29dd70-6f0b-42e2-95ad-d4e3fdd76613;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsElevator";
							- _id = GUID 31699188-f497-44da-ba21-a224d2fec074;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID cb792d8a-847b-405f-9cb0-ef14d9e28165;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 698 381.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID bd949283-a5c3-46cf-a805-357b1ca5fadd;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 747 375.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID 3f6991cb-e0b9-46fc-92e6-a3dc5077bded;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000446689 0 0 0.000261456 842 379.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIActiveX 
					- _id = GUID 917b6cdf-1d9a-4b8a-b460-d2db34d15eb9;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 0.000126238 0 0 0.000113298 914 388.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.SystemController[0].itsFloor[1].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "SystemController";
							- _name = "itsFloor";
							- _id = GUID 494c5a0f-2be7-4b8d-8b85-5b091b455f2d;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "SystemController";
							- _id = GUID 9f3e0989-e423-422d-8974-a567a0753238;
						}
					}
				}
				{ CGIFreeText 
					- _id = GUID f23e446b-ce2f-4de4-8228-c3398dfb7c9a;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
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
					- m_transform = 1 0 0 1 -58 -58 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1103 445  1103 463  1037 463  ;
					- m_text = "Ground";
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 5f677aa3-a232-4d88-b675-f23cb2f4c609;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
			}
		}
		{ IPanelDiagram 
			- _id = GUID 245b8851-1933-44f0-a890-1fac304a7595;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
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
										- _Name = "PanelControlTypeBindingDisplay";
										- _Value = "All";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,PredefinedOnly";
									}
								}
							}
						}
					}
				}
			}
			- _name = "panel2";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "9.18.2015::14:24:14";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 72699eaf-700f-4c7f-b5ae-7cb248207643;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IPanelDiagram";
					- _id = GUID 245b8851-1933-44f0-a890-1fac304a7595;
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
				- elementList = 40;
				{ CGIBox 
					- _id = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
					- m_type = 215;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Default.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Default";
						- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
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
					- _id = GUID bca9eecd-5a23-4ff0-8042-ceeef42059dd;
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
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;12632256;CurrentValue;5;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;7.8;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;5;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;.2;RelativeHeight;.9;RelativeWidth;.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
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
										- _Name = "LevelIndicator";
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
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "Elevator";
						- _name = "currentLevel";
						- _id = GUID a37ba97e-ef57-4eb3-bb8d-ab77cb65336d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.00116527 0 0 0.00139443 81 115.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Elevator[0].currentLevel";
					- m_csName = "levelindicator_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 22d618e7-807d-4523-8ff5-b13c78dafd69;
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
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
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
						- _id = GUID a37ba97e-ef57-4eb3-bb8d-ab77cb65336d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000407846 0 0 0.000278887 124 50.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Elevator[0].currentLevel";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 444a78b4-4bed-4528-a3bf-9e40a1557b4b;
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
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 733 238.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 0;
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID a452f488-85b0-4663-b6d7-fde2e5a1c351;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 731 290.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID 1c559dd6-cbc1-4cd3-9532-70622bd9c46d;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 731 336.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIMFCCtrl 
					- _id = GUID 9cfc0f00-eac3-4f57-a7b1-f84aa443c025;
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
						- _id = GUID 08e3f5a6-1167-4d68-8d33-33e58d2d8e6c;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 732 394.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[0].evUpButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Up";
				}
				{ CGIActiveX 
					- _id = GUID 14422c4d-2113-4b3a-a6a5-9020f8b134c8;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 681 243.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.abLevel[3].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 7d93a526-c087-4fc1-b0c2-0b9854fab485;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 681 296.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID c7ef8060-01a8-4e00-b0e3-876ead1969ae;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 681 341.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID b60d5421-4a65-4221-8783-52e89815f6fd;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "up";
						- _id = GUID 9a696093-65c3-4866-b532-13ef1711caaf;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 681 401.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[0].up";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID a68a7332-efcc-45b7-b8f9-780c0f0801d7;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 825 192.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[4].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID e5ab71b2-95d7-48bd-901a-0b93b36641eb;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 828 239.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[3].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID ad8f5247-77a5-46a4-acf4-3cd28aa27b43;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 826 288.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIMFCCtrl 
					- _id = GUID e6a4d6f7-3047-4a2a-a6f9-b862be1c3329;
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
						- _id = GUID ddf588a5-6409-4f2e-8a9b-7155052d21a6;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000446689 0 0 0.000261456 827 334.291 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].evDownButton";
					- m_csName = "pushbutton_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "Down";
				}
				{ CGIActiveX 
					- _id = GUID cdd26cd0-ab7e-44da-84ef-be15e2283579;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 894 200.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[4].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID fb597b9a-d042-4f06-b585-9e9885f72676;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 897 247.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[3].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 66da270c-fc5a-4326-b81e-4ceb4a9ee760;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 897 297.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 7c77dde6-2f44-492b-83f7-6aadbcef17d0;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "down";
						- _id = GUID 8445c603-526b-486c-bcee-c7b2e4febe0d;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 897 342.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].down";
					- m_csName = "led_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID bff2a21a-4f0f-41d1-b272-eed8cf244474;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
					- m_name = { CGIText 
						- m_str = "door open";
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
					- m_transform = 0.000126238 0 0 0.000113298 60 64.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "";
					- m_csName = "door open";
					- m_PartsArray = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID f71b2af4-7a60-4770-a662-38db269e1478;
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
						- _name = "evLevelOn()";
						- _id = GUID 0c00c6b5-4ba3-4351-8f88-f6591d4110c7;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000427267 0 0 0.000287602 274 213.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[0].evLevelOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "G";
				}
				{ CGIMFCCtrl 
					- _id = GUID 1f52fb8c-d472-4be3-9b3b-46bb46f92f80;
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
						- _id = GUID 7253a803-db22-4647-9a13-5f143b3db28c;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000582637 0 0 0.000313747 402 115.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Elevator[0].evClose";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
						}
					}
					- m_csButtonCaption = ">>|<<";
				}
				{ CGIMFCCtrl 
					- _id = GUID f01c65d0-db2b-482b-93bf-e09adba76a34;
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
						- _id = GUID 590591ec-aa3d-4bdb-9ba5-58ff6a90585b;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000582637 0 0 0.000313747 404 59.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Elevator[0].evOpen";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
						}
					}
					- m_csButtonCaption = "<<|>>";
				}
				{ CGIFreeText 
					- _id = GUID 6a039b85-e26e-4cbb-9119-80fecce71563;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 1 0 0 1 -69 -51 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1084 445  1084 467  1037 467  ;
					- m_text = "Level 1";
				}
				{ CGIFreeText 
					- _id = GUID ccc28847-33f5-406c-82d4-743ada81749c;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 1 0 0 1 -70 -104 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 2";
				}
				{ CGIFreeText 
					- _id = GUID 418221c2-de82-42c6-893e-8d8918396b79;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 1 0 0 1 -70 -150 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 3";
				}
				{ CGIFreeText 
					- _id = GUID d8fa1d88-32d8-44c7-a7ce-8b5adbca0a79;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 1 0 0 1 -71 -200 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 4";
				}
				{ CGIFreeText 
					- _id = GUID 2b02ef99-6d25-429b-a22c-0f974986bb21;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 1 0 0 1 -71 -248 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 1037 445  1107 445  1107 467  1037 467  ;
					- m_text = "Level 5";
				}
				{ CGIMFCCtrl 
					- _id = GUID d752a965-35de-4581-a6d8-13574ea32996;
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
						- _name = "evLevelOn()";
						- _id = GUID 0c00c6b5-4ba3-4351-8f88-f6591d4110c7;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000427267 0 0 0.000287602 276 173.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].evLevelOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "2";
				}
				{ CGIMFCCtrl 
					- _id = GUID 3fcedb1e-d87c-48f2-b632-eb62a87f9028;
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
						- _name = "evLevelOn()";
						- _id = GUID 0c00c6b5-4ba3-4351-8f88-f6591d4110c7;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000427267 0 0 0.000287602 276 133.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].evLevelOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "3";
				}
				{ CGIMFCCtrl 
					- _id = GUID 77281ab7-0666-41d8-b899-3e1249304b66;
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
						- _name = "evLevelOn()";
						- _id = GUID 0c00c6b5-4ba3-4351-8f88-f6591d4110c7;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000427267 0 0 0.000287602 274 94.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[3].evLevelOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "4";
				}
				{ CGIMFCCtrl 
					- _id = GUID ccd4bead-43a6-4ddd-9b6c-91aaa8c4678f;
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
						- _name = "evLevelOn()";
						- _id = GUID 0c00c6b5-4ba3-4351-8f88-f6591d4110c7;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000427267 0 0 0.000287602 273 53.32 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[4].evLevelOn";
					- m_csName = "pushbutton_8";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
					- m_csButtonCaption = "5";
				}
				{ CGIActiveX 
					- _id = GUID a2d18f1e-6586-4784-ba97-ea9d17f35aa0;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "level";
						- _id = GUID adfa595f-e8b2-40a1-b878-0bc09dcf60f5;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 340 105.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[3].level";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 573164d0-36d1-4914-af28-444782f24337;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "level";
						- _id = GUID adfa595f-e8b2-40a1-b878-0bc09dcf60f5;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 339 64.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[4].level";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 19b7a8d8-ee4b-4465-9aaa-f817a08c79a2;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "level";
						- _id = GUID adfa595f-e8b2-40a1-b878-0bc09dcf60f5;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 341 141.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[2].level";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 98920557-5eae-4051-8712-261c5dbb96eb;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "level";
						- _id = GUID adfa595f-e8b2-40a1-b878-0bc09dcf60f5;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 339 222.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[0].level";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 2b90a261-85f5-477a-af61-9ef8b879fa5a;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
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
						- _class = "Floor";
						- _name = "level";
						- _id = GUID adfa595f-e8b2-40a1-b878-0bc09dcf60f5;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 340 182.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Floor[1].level";
					- m_csName = "led_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Floor";
							- _id = GUID 54e4cb9c-0f47-47f8-9a8b-139afb747bdf;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID bb551eb9-de47-4d3c-a8c8-d639437c234a;
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
						- _id = GUID 8f53ccbd-27ac-4b3b-ae3b-675639e35a80;
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000582637 0 0 0.000313747 404 165.35 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "Default.Elevator[0].evAlarm";
					- m_csName = "pushbutton_9";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "";
							- _name = "Elevator";
							- _id = GUID ccc65604-a30e-4f05-a612-b575200a91ec;
						}
					}
					- m_csButtonCaption = "Alarm";
				}
				{ CGIActiveX 
					- _id = GUID 21a2bdc5-db28-4cab-bae0-0bd1b97dda31;
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
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
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
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.000126238 0 0 0.000113298 430 214.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "";
					- m_csName = "led_14";
					- m_PartsArray = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIActiveX 
					- _id = GUID 97b9f33b-fb0c-49cb-910d-48b454bc2bdf;
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
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;12632256;CurrentValue;5;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;7.8;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;5;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;.2;RelativeHeight;.9;RelativeWidth;.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
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
										- _Name = "LevelIndicator";
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
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
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
					- m_transform = 0.00116527 0 0 0.00139443 90 406.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "";
					- m_csName = "levelindicator_1";
					- m_PartsArray = { IRPYRawContainer 
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
				- m_pRoot = GUID 98ded2d7-703b-40ea-aa4e-6d73bff36f1d;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 2b1bfd46-f404-466a-af64-ee8e7ff13c39;
			}
		}
	}
}

