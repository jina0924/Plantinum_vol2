<%@page import="java.io.InputStream"%>
<%@page import="java.net.URLEncoder"%>
<%@page import="org.w3c.dom.NodeList"%>
<%@page import="org.w3c.dom.Node"%>
<%@page import="org.w3c.dom.Element"%>
<%@page import="javax.xml.parsers.DocumentBuilderFactory"%>
<%@page import="org.w3c.dom.Document"%>
<%@page import="java.net.URL"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>실내정원용 식물</title>
</head>
<body>
<h4><strong> * 샘플화면은 디자인을 적용하지 않았으니, 개별 사이트의 스타일에 맞게 코딩하시기 바랍니다.</strong></h4>
<h3><strong>실내정원용 식물</strong></h3>
<hr>
<%
//인테러뱅 상세조회

	//apiKey - 농사로 Open API에서 신청 후 승인되면 확인 가능
	String apiKey="인증키를입력하세요";
	//서비스 명
	String serviceName="garden";
	//오퍼레이션 명
	String operationName="gardenDtl";
	
	//XML 받을 URL 생성
	String parameter = "/"+serviceName+"/"+operationName;
	parameter += "?apiKey="+ apiKey;
	parameter += "&cntntsNo="+ request.getParameter("cntntsNo");
	
	//서버와 통신
	URL apiUrl = new URL("http://api.nongsaro.go.kr/service"+parameter);
	InputStream apiStream = apiUrl.openStream();
	
	Document doc = null;
	try{
		//xml document
		doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(apiStream);
	}catch(Exception e){
		e.printStackTrace();
	}finally{
		apiStream.close();
	}
	String resultCode="";
	String resultMsg="";
	try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
	try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
	
	
	//콘텐츠 번로 
	String cntntsNo             =""; 
	//식물 학명         
	String plntbneNm            =""; 
	//식물 영명        
	String plntzrNm             =""; 
	//유통 명                 
	String distbNm              =""; 
	//과명                  
	String fmlNm                =""; 
	//원산지 명           
	String orgplceInfo          =""; 
	//조언 정보                  
	String adviseInfo           =""; 
	//이미지 평가 링크 명          
	String imageEvlLinkCours    =""; 
	//성장 높이 정보               
	String growthHgInfo         =""; 
	//성장 넓이 정보              
	String growthAraInfo        =""; 
	//잎 형태 정보             
	String lefStleInfo          =""; 
	//냄새 코드               
	String smellCode            =""; 
	//독정 정보                 
	String toxctyInfo           =""; 
	//번식 시기             
	String prpgtEraInfo         =""; 
	//기타 시기 정보             
	String etcEraInfo           =""; 
	//관리수준 코드          
	String managelevelCode      =""; 
	//생장속도 코드             
	String grwtveCode           =""; 
	//생육 온도 코드        
	String grwhTpCode           =""; 
	//겨울 최저 온도 코드         
	String winterLwetTpCode     =""; 
	//습도 코드    
	String hdCode               =""; 
	//비료 정보                 
	String frtlzrInfo           =""; 
	//토양 정보           
	String soilInfo             =""; 
	//물주기 봄 코드          
	String watercycleSprngCode  =""; 
	//물주기 여름 코드            
	String watercycleSummerCode =""; 
	//물주기 가을 코드            
	String watercycleAutumnCode =""; 
	//물주기 겨울 코드               
	String watercycleWinterCode =""; 
	//병충해 관리 정보          
	String dlthtsManageInfo     =""; 
	//특별관리 정보              
	String speclmanageInfo      =""; 
	//기능성 정보                 
	String fncltyInfo           =""; 
	//화분직경 대 정보       
	String flpodmtBigInfo       =""; 
	//화분직경 중 정보              
	String flpodmtMddlInfo      =""; 
	//화분직경 소 정보                
	String flpodmtSmallInfo     =""; 
	//가로 대 정보                  
	String widthBigInfo         =""; 
	//가로 중 정보                 
	String widthMddlInfo        =""; 
	//가로 소 정보                  
	String widthSmallInfo       =""; 
	//세로 대 정보                 
	String vrticlBigInfo        =""; 
	//세로 중 정보                
	String vrticlMddlInfo       =""; 
	//세로 소 정보                   
	String vrticlSmallInfo      =""; 
	//높이 대 정보                 
	String hgBigInfo            =""; 
	//높이 중 정보                    
	String hgMddlInfo           =""; 
	//높이 소 정보                  
	String hgSmallInfo          =""; 
	//볼륨 대 정보                   
	String volmeBigInfo         =""; 
	//볼륨 중 정보                   
	String volmeMddlInfo        =""; 
	//볼륨 소 정보                  
	String volmeSmallInfo       =""; 
	//가격 대 정보                
	String pcBigInfo            =""; 
	//가격 중 정보               
	String pcMddlInfo           =""; 
	//가격 소 정보                
	String pcSmallInfo          =""; 
	//관리요구도 코드                  
	String managedemanddoCode   =""; 
	
	try{cntntsNo             = doc.getElementsByTagName("cntntsNo").item(0).getFirstChild().getNodeValue();             }catch(Exception e){cntntsNo             = "";}
	try{plntbneNm            = doc.getElementsByTagName("plntbneNm").item(0).getFirstChild().getNodeValue();            }catch(Exception e){plntbneNm            = "";}
	try{plntzrNm             = doc.getElementsByTagName("plntzrNm").item(0).getFirstChild().getNodeValue();             }catch(Exception e){plntzrNm             = "";}
	try{distbNm              = doc.getElementsByTagName("distbNm").item(0).getFirstChild().getNodeValue();              }catch(Exception e){distbNm              = "";}
	try{fmlNm                = doc.getElementsByTagName("fmlNm").item(0).getFirstChild().getNodeValue();                }catch(Exception e){fmlNm                = "";}
	try{orgplceInfo          = doc.getElementsByTagName("orgplceInfo").item(0).getFirstChild().getNodeValue();          }catch(Exception e){orgplceInfo          = "";}
	try{adviseInfo           = doc.getElementsByTagName("adviseInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){adviseInfo           = "";}
	try{imageEvlLinkCours    = doc.getElementsByTagName("imageEvlLinkCours").item(0).getFirstChild().getNodeValue();    }catch(Exception e){imageEvlLinkCours    = "";}
	try{growthHgInfo         = doc.getElementsByTagName("growthHgInfo").item(0).getFirstChild().getNodeValue();         }catch(Exception e){growthHgInfo         = "";}
	try{growthAraInfo        = doc.getElementsByTagName("growthAraInfo").item(0).getFirstChild().getNodeValue();        }catch(Exception e){growthAraInfo        = "";}
	try{lefStleInfo          = doc.getElementsByTagName("lefStleInfo").item(0).getFirstChild().getNodeValue();          }catch(Exception e){lefStleInfo          = "";}
	try{smellCode            = doc.getElementsByTagName("smellCode").item(0).getFirstChild().getNodeValue();            }catch(Exception e){smellCode            = "";}
	try{toxctyInfo           = doc.getElementsByTagName("toxctyInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){toxctyInfo           = "";}
	try{prpgtEraInfo         = doc.getElementsByTagName("prpgtEraInfo").item(0).getFirstChild().getNodeValue();         }catch(Exception e){prpgtEraInfo         = "";}
	try{etcEraInfo           = doc.getElementsByTagName("etcEraInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){etcEraInfo           = "";}
	try{managelevelCode      = doc.getElementsByTagName("managelevelCode").item(0).getFirstChild().getNodeValue();      }catch(Exception e){managelevelCode      = "";}
	try{grwtveCode           = doc.getElementsByTagName("grwtveCode").item(0).getFirstChild().getNodeValue();           }catch(Exception e){grwtveCode           = "";}
	try{grwhTpCode           = doc.getElementsByTagName("grwhTpCode").item(0).getFirstChild().getNodeValue();           }catch(Exception e){grwhTpCode           = "";}
	try{winterLwetTpCode     = doc.getElementsByTagName("winterLwetTpCode").item(0).getFirstChild().getNodeValue();     }catch(Exception e){winterLwetTpCode     = "";}
	try{hdCode               = doc.getElementsByTagName("hdCode").item(0).getFirstChild().getNodeValue();               }catch(Exception e){hdCode               = "";}
	try{frtlzrInfo           = doc.getElementsByTagName("frtlzrInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){frtlzrInfo           = "";}
	try{soilInfo             = doc.getElementsByTagName("soilInfo").item(0).getFirstChild().getNodeValue();             }catch(Exception e){soilInfo             = "";}
	try{watercycleSprngCode  = doc.getElementsByTagName("watercycleSprngCode").item(0).getFirstChild().getNodeValue();  }catch(Exception e){watercycleSprngCode  = "";}
	try{watercycleSummerCode = doc.getElementsByTagName("watercycleSummerCode").item(0).getFirstChild().getNodeValue(); }catch(Exception e){watercycleSummerCode = "";}
	try{watercycleAutumnCode = doc.getElementsByTagName("watercycleAutumnCode").item(0).getFirstChild().getNodeValue(); }catch(Exception e){watercycleAutumnCode = "";}
	try{watercycleWinterCode = doc.getElementsByTagName("watercycleWinterCode").item(0).getFirstChild().getNodeValue(); }catch(Exception e){watercycleWinterCode = "";}
	try{dlthtsManageInfo     = doc.getElementsByTagName("dlthtsManageInfo").item(0).getFirstChild().getNodeValue();     }catch(Exception e){dlthtsManageInfo     = "";}
	try{speclmanageInfo      = doc.getElementsByTagName("speclmanageInfo").item(0).getFirstChild().getNodeValue();      }catch(Exception e){speclmanageInfo      = "";}
	try{fncltyInfo           = doc.getElementsByTagName("fncltyInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){fncltyInfo           = "";}
	try{flpodmtBigInfo       = doc.getElementsByTagName("flpodmtBigInfo").item(0).getFirstChild().getNodeValue();       }catch(Exception e){flpodmtBigInfo       = "";}
	try{flpodmtMddlInfo      = doc.getElementsByTagName("flpodmtMddlInfo").item(0).getFirstChild().getNodeValue();      }catch(Exception e){flpodmtMddlInfo      = "";}
	try{flpodmtSmallInfo     = doc.getElementsByTagName("flpodmtSmallInfo").item(0).getFirstChild().getNodeValue();     }catch(Exception e){flpodmtSmallInfo     = "";}
	try{widthBigInfo         = doc.getElementsByTagName("widthBigInfo").item(0).getFirstChild().getNodeValue();         }catch(Exception e){widthBigInfo         = "";}
	try{widthMddlInfo        = doc.getElementsByTagName("widthMddlInfo").item(0).getFirstChild().getNodeValue();        }catch(Exception e){widthMddlInfo        = "";}
	try{widthSmallInfo       = doc.getElementsByTagName("widthSmallInfo").item(0).getFirstChild().getNodeValue();       }catch(Exception e){widthSmallInfo       = "";}
	try{vrticlBigInfo        = doc.getElementsByTagName("vrticlBigInfo").item(0).getFirstChild().getNodeValue();        }catch(Exception e){vrticlBigInfo        = "";}
	try{vrticlMddlInfo       = doc.getElementsByTagName("vrticlMddlInfo").item(0).getFirstChild().getNodeValue();       }catch(Exception e){vrticlMddlInfo       = "";}
	try{vrticlSmallInfo      = doc.getElementsByTagName("vrticlSmallInfo").item(0).getFirstChild().getNodeValue();      }catch(Exception e){vrticlSmallInfo      = "";}
	try{hgBigInfo            = doc.getElementsByTagName("hgBigInfo").item(0).getFirstChild().getNodeValue();            }catch(Exception e){hgBigInfo            = "";}
	try{hgMddlInfo           = doc.getElementsByTagName("hgMddlInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){hgMddlInfo           = "";}
	try{hgSmallInfo          = doc.getElementsByTagName("hgSmallInfo").item(0).getFirstChild().getNodeValue();          }catch(Exception e){hgSmallInfo          = "";}
	try{volmeBigInfo         = doc.getElementsByTagName("volmeBigInfo").item(0).getFirstChild().getNodeValue();         }catch(Exception e){volmeBigInfo         = "";}
	try{volmeMddlInfo        = doc.getElementsByTagName("volmeMddlInfo").item(0).getFirstChild().getNodeValue();        }catch(Exception e){volmeMddlInfo        = "";}
	try{volmeSmallInfo       = doc.getElementsByTagName("volmeSmallInfo").item(0).getFirstChild().getNodeValue();       }catch(Exception e){volmeSmallInfo       = "";}
	try{pcBigInfo            = doc.getElementsByTagName("pcBigInfo").item(0).getFirstChild().getNodeValue();            }catch(Exception e){pcBigInfo            = "";}
	try{pcMddlInfo           = doc.getElementsByTagName("pcMddlInfo").item(0).getFirstChild().getNodeValue();           }catch(Exception e){pcMddlInfo           = "";}
	try{pcSmallInfo          = doc.getElementsByTagName("pcSmallInfo").item(0).getFirstChild().getNodeValue();          }catch(Exception e){pcSmallInfo          = "";}
	try{managedemanddoCode   = doc.getElementsByTagName("managedemanddoCode").item(0).getFirstChild().getNodeValue();   }catch(Exception e){managedemanddoCode   = "";}
	
	if(resultCode.equals("00")){
%>
	<table  border="1" cellspacing="0" cellpadding="0">
		<colgroup>
			<col width="15%">
			<col width="*">
		</colgroup>
		<tr>
            <th>식물학명</th>
            <td><%=plntbneNm%></td>
        </tr>
        <tr>
            <th>식물영명</th>
            <td><%=plntzrNm%></td>
        </tr>
        <tr>
            <th>유통명</th>
            <td><%=distbNm%></td>
        </tr>
        <tr>
            <th>과명</th>
            <td><%=fmlNm%></td>
        </tr>
        <tr>
            <th>원산지 정보</th>
            <td><%=orgplceInfo%></td>
        </tr>
        <tr>
            <th>조언 정보</th>
            <td><%=adviseInfo%></td>
        </tr>
        <tr>
            <th>이미지 평가 링크 경로</th>
            <td><%=imageEvlLinkCours%></td>
        </tr>
        <tr>
            <th>성장 높이 정보</th>
            <td><%=growthHgInfo%></td>
        </tr>
        <tr>
            <th>성장 넓이 정보</th>
            <td><%=growthAraInfo%></td>
        </tr>
        <tr>
            <th>잎 형태 정보</th>
            <td><%=lefStleInfo%></td>
        </tr>
        <tr>
            <th>냄새 코드</th>
            <td><%=smellCode%></td>
        </tr>
        <tr>
            <th>독성 정보</th>
            <td><%=toxctyInfo%></td>
        </tr>
        <tr>
            <th>번식 시기 정보</th>
            <td><%=prpgtEraInfo%></td>
        </tr>
        <tr>
            <th>기타 시기 정보</th>
            <td><%=etcEraInfo%></td>
        </tr>
        <tr>
            <th>관리수준 코드</th>
            <td><%=managelevelCode%></td>
        </tr>
        <tr>
            <th>생장속도 코드</th>
            <td><%=grwtveCode%></td>
        </tr>
        <tr>
            <th>생육 온도 코드</th>
            <td><%=grwhTpCode%></td>
        </tr>
        <tr>
            <th>겨울 최저 온도 코드</th>
            <td><%=winterLwetTpCode%></td>
        </tr>
        <tr>
            <th>습도 코드</th>
            <td><%=hdCode%></td>
        </tr>
        <tr>
            <th>비료 정보</th>
            <td><%=frtlzrInfo%></td>
        </tr>
        <tr>
            <th>토양 정보</th>
            <td><%=soilInfo%></td>
        </tr>
        <tr>
            <th>물주기 봄 코드</th>
            <td><%=watercycleSprngCode%></td>
        </tr>
        <tr>
            <th>물주기 여름 코드</th>
            <td><%=watercycleSummerCode%></td>
        </tr>
        <tr>
            <th>물주기 가을 코드</th>
            <td><%=watercycleAutumnCode%></td>
        </tr>
        <tr>
            <th>물주기 겨울 코드</th>
            <td><%=watercycleWinterCode%></td>
        </tr>
        <tr>
            <th>병충해 관리 정보</th>
            <td><%=dlthtsManageInfo%></td>
        </tr>
        <tr>
            <th>특별관리 정보</th>
            <td><%=speclmanageInfo%></td>
        </tr>
        <tr>
            <th>기능성 정보</th>
            <td><%=fncltyInfo%></td>
        </tr>
        <tr>
            <th>화분직경 대 정보</th>
            <td><%=flpodmtBigInfo%></td>
        </tr>
        <tr>
            <th>화분직경 중 정보</th>
            <td><%=flpodmtMddlInfo%></td>
        </tr>
        <tr>
            <th>화분직경 소 정보</th>
            <td><%=flpodmtSmallInfo%></td>
        </tr>
        <tr>
            <th>가로 대 정보</th>
            <td><%=widthBigInfo%></td>
        </tr>
        <tr>
            <th>가로 중 정보</th>
            <td><%=widthMddlInfo%></td>
        </tr>
        <tr>
            <th>가로 소 정보</th>
            <td><%=widthSmallInfo%></td>
        </tr>
        <tr>
            <th>세로 대 정보</th>
            <td><%=vrticlBigInfo%></td>
        </tr>
        <tr>
            <th>세로 중 정보</th>
            <td><%=vrticlMddlInfo%></td>
        </tr>
        <tr>
            <th>세로 소 정보</th>
            <td><%=vrticlSmallInfo%></td>
        </tr>
        <tr>
            <th>높이 대 정보</th>
            <td><%=hgBigInfo%></td>
        </tr>
        <tr>
            <th>높이 중 정보</th>
            <td><%=hgMddlInfo%></td>
        </tr>
        <tr>
            <th>높이 소 정보</th>
            <td><%=hgSmallInfo%></td>
        </tr>
        <tr>
            <th>볼륨 대 정보</th>
            <td><%=volmeBigInfo%></td>
        </tr>
        <tr>
            <th>볼륨 중 정보</th>
            <td><%=volmeMddlInfo%></td>
        </tr>
        <tr>
            <th>볼륨 소 정보</th>
            <td><%=volmeSmallInfo%></td>
        </tr>
        <tr>
            <th>가격 대 정보</th>
            <td><%=pcBigInfo%></td>
        </tr>
        <tr>
            <th>가격 중 정보</th>
            <td><%=pcMddlInfo%></td>
        </tr>
        <tr>
            <th>가격 소 정보</th>
            <td><%=pcSmallInfo%></td>
        </tr>
        <tr>
            <th>관리요구도 코드</th>
            <td><%=managedemanddoCode%></td>
        </tr>
	</table>
<%
	}else{
		out.println(resultMsg);
	}
%>
<input type="button" onclick="javascript:fncList();" value="목록"/>
<form name="searchApiForm">
<%
String[] searchNmArr = {"pageNo", "sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel"};
for(int i=0; i<searchNmArr.length; i++){
	out.println("<input type='hidden' name='"+searchNmArr[i]+"' value='"+request.getParameter(searchNmArr[i])+"' />");
}
%>
</form>
<script type="text/javascript">
//목록이동
function fncList(){
	with(document.searchApiForm){
		method="get";
		action = "gardenList.jsp";
		target = "_self";
		submit();
	}
}
</script>
</body>
</html>