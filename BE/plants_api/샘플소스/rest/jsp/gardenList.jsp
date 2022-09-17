<%@page import="java.util.HashMap"%>
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
<script type="text/javascript">
//상세보기
function fncDtl(cNo){
	with(document.searchApiForm){
		cntntsNo.value = cNo;
		method="get";
		action = "gardenDtl.jsp";
		target = "_self";
		submit();
	}
}

//검색
function fncSearch(){
	with(document.searchApiForm){
		lightChkVal.value = fncCheckValue(document.getElementsByName("lightChk"));
		grwhstleChkVal.value = fncCheckValue(document.getElementsByName("grwhstleChk"));
		lefcolrChkVal.value = fncCheckValue(document.getElementsByName("lefcolrChk"));
		lefmrkChkVal.value = fncCheckValue(document.getElementsByName("lefmrkChk"));
		flclrChkVal.value = fncCheckValue(document.getElementsByName("flclrChk"));
		fmldecolrChkVal.value = fncCheckValue(document.getElementsByName("fmldecolrChk"));
		ignSeasonChkVal.value = fncCheckValue(document.getElementsByName("ignSeasonChk"));
		winterLwetChkVal.value = fncCheckValue(document.getElementsByName("winterLwetChk"));
		pageNo.value = "1";
		method="get";
		action = "gardenList.jsp";
		target = "_self";
		submit();
	}
}
//페이지 이동
function fncGoPage(page){
	with(document.searchApiForm){
		pageNo.value = page;
		method="get";
		action = "gardenList.jsp";
		target = "_self";
		submit();
	}
}

function fncWordTypeOption(){
	var wordType = document.getElementById("wordType")[document.getElementById("wordType").selectedIndex].value;

 	if(wordType == "cntntsSj"){
 		document.getElementById("englishSrch").style.display="none";
 		document.getElementById("koreanSrch").style.display="block";
	}else if(wordType == "plntbneNm"){
 		document.getElementById("koreanSrch").style.display="none";
 		document.getElementById("englishSrch").style.display="block";
	}
}

function fncContSearch(word){
	document.searchApiForm.word.value = word;
	fncSearch();
}

function fncCheckValue(obj){
	var checkValue = "";

	for(var i=0; i<obj.length; i++){
		if(obj[i].checked == true){
			checkValue += obj[i].value + ",";
		}
	}

	if(checkValue!="") checkValue = checkValue.substring(0, checkValue.length-1);

	return checkValue;
}

</script>
</head>
<body>
<h4><strong> * 샘플화면은 디자인을 적용하지 않았으니, 개별 사이트의 스타일에 맞게 코딩하시기 바랍니다.</strong></h4>
<h3><strong>실내정원용 식물</strong></h3>
<hr>
<% 
String sType = request.getParameter("sType")==null?"":request.getParameter("sType"); 
String wordType = request.getParameter("wordType")==null?"":request.getParameter("wordType"); 
String word = request.getParameter("word")==null?"":request.getParameter("word"); 
String priceType = request.getParameter("priceType")==null?"":request.getParameter("priceType"); 
String priceTypeSel = request.getParameter("priceTypeSel")==null?"":request.getParameter("priceTypeSel"); 
String waterCycleSel = request.getParameter("waterCycleSel")==null?"":request.getParameter("waterCycleSel"); 
%>
<form name="searchApiForm">
<input type="hidden" name="cntntsNo">
<input type="hidden" name="pageNo" value="<%=request.getParameter("pageNo")==null?"":request.getParameter("pageNo")%>">
<input type="hidden" name="word" value="<%=request.getParameter("word")==null?"":request.getParameter("word")%>">
<input type="hidden" name="lightChkVal" value="<%=request.getParameter("lightChkVal")==null?"":request.getParameter("lightChkVal")%>">
<input type="hidden" name="grwhstleChkVal" value="<%=request.getParameter("grwhstleChkVal")==null?"":request.getParameter("grwhstleChkVal")%>">
<input type="hidden" name="lefcolrChkVal" value="<%=request.getParameter("lefcolrChkVal")==null?"":request.getParameter("lefcolrChkVal")%>">
<input type="hidden" name="lefmrkChkVal" value="<%=request.getParameter("lefmrkChkVal")==null?"":request.getParameter("lefmrkChkVal")%>">
<input type="hidden" name="flclrChkVal" value="<%=request.getParameter("flclrChkVal")==null?"":request.getParameter("flclrChkVal")%>">
<input type="hidden" name="fmldecolrChkVal" value="<%=request.getParameter("fmldecolrChkVal")==null?"":request.getParameter("fmldecolrChkVal")%>">
<input type="hidden" name="ignSeasonChkVal" value="<%=request.getParameter("ignSeasonChkVal")==null?"":request.getParameter("ignSeasonChkVal")%>">
<input type="hidden" name="winterLwetChkVal" value="<%=request.getParameter("winterLwetChkVal")==null?"":request.getParameter("winterLwetChkVal")%>">
<table width="100%" border="1" cellSpacing="0" cellPadding="0">
	<colgroup>
		<col width="20%"/>
		<col width="80%"/>
	</colgroup>
	<tr>
		<th>
			<select name="sType"> 
				<option value="sCntntsSj" <%=sType.equals("sCntntsSj")?"selected":""%>>식물명</option>
				<option value="sPlntbneNm" <%=sType.equals("sPlntbneNm")?"selected":""%>>한명</option>
				<option value="sPlntzrNm" <%=sType.equals("sPlntzrNm")?"selected":""%>>영명</option>
			</select> 
		</th>
		<td>
			<input type="text" name="sText" value="<%=request.getParameter("sText")==null?"":request.getParameter("sText")%>">
			<input type="button" name="search" value="검색" onclick="return fncSearch();"/>
		</td>
	</tr>
	<tr>
		<th>
			<select id="wordType" name="wordType" onchange="javascript:fncWordTypeOption(); return false;">
				<option value="cntntsSj" <%=wordType.equals("cntntsSj")?"selected":""%>>국명</option>
				<option value="plntbneNm" <%=wordType.equals("plntbneNm")?"selected":""%>>학명</option>
			</select>
		</th>
		<td>
			<div id="koreanSrch" style="display: <%= wordType.equals("") ? "block" : wordType.equals("cntntsSj")?"block":"none"%>;">
				<a href="#" onclick="javascript:fncContSearch('ㄱ');return false;" style="font-weight:<%=word.equals("ㄱ")?"bold":"" %>">ㄱ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄴ');return false;" style="font-weight:<%=word.equals("ㄴ")?"bold":"" %>">ㄴ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄷ');return false;" style="font-weight:<%=word.equals("ㄷ")?"bold":"" %>">ㄷ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄹ');return false;" style="font-weight:<%=word.equals("ㄹ")?"bold":"" %>">ㄹ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅁ');return false;" style="font-weight:<%=word.equals("ㅁ")?"bold":"" %>">ㅁ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅂ');return false;" style="font-weight:<%=word.equals("ㅂ")?"bold":"" %>">ㅂ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅅ');return false;" style="font-weight:<%=word.equals("ㅅ")?"bold":"" %>">ㅅ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅇ');return false;" style="font-weight:<%=word.equals("ㅇ")?"bold":"" %>">ㅇ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅈ');return false;" style="font-weight:<%=word.equals("ㅈ")?"bold":"" %>">ㅈ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅊ');return false;" style="font-weight:<%=word.equals("ㅊ")?"bold":"" %>">ㅊ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅋ');return false;" style="font-weight:<%=word.equals("ㅋ")?"bold":"" %>">ㅋ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅌ');return false;" style="font-weight:<%=word.equals("ㅌ")?"bold":"" %>">ㅌ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅍ');return false;" style="font-weight:<%=word.equals("ㅍ")?"bold":"" %>">ㅍ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅎ');return false;" style="font-weight:<%=word.equals("ㅎ")?"bold":"" %>">ㅎ</a>
			</div>
			<div id="englishSrch" style="display: <%=wordType.equals("plntbneNm")?"block":"none"%>;">
				<a href="#" onclick="javascript:fncContSearch('A');return false;" style="font-weight:<%=word.equals("A")?"bold":"" %>">A</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('B');return false;" style="font-weight:<%=word.equals("B")?"bold":"" %>">B</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('C');return false;" style="font-weight:<%=word.equals("C")?"bold":"" %>">C</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('D');return false;" style="font-weight:<%=word.equals("D")?"bold":"" %>">D</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('E');return false;" style="font-weight:<%=word.equals("E")?"bold":"" %>">E</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('F');return false;" style="font-weight:<%=word.equals("F")?"bold":"" %>">F</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('G');return false;" style="font-weight:<%=word.equals("G")?"bold":"" %>">G</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('H');return false;" style="font-weight:<%=word.equals("H")?"bold":"" %>">H</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('I');return false;" style="font-weight:<%=word.equals("I")?"bold":"" %>">I</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('J');return false;" style="font-weight:<%=word.equals("J")?"bold":"" %>">J</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('K');return false;" style="font-weight:<%=word.equals("K")?"bold":"" %>">K</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('L');return false;" style="font-weight:<%=word.equals("L")?"bold":"" %>">L</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('M');return false;" style="font-weight:<%=word.equals("M")?"bold":"" %>">M</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('N');return false;" style="font-weight:<%=word.equals("N")?"bold":"" %>">N</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('O');return false;" style="font-weight:<%=word.equals("O")?"bold":"" %>">O</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('P');return false;" style="font-weight:<%=word.equals("P")?"bold":"" %>">P</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Q');return false;" style="font-weight:<%=word.equals("Q")?"bold":"" %>">Q</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('R');return false;" style="font-weight:<%=word.equals("R")?"bold":"" %>">R</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('S');return false;" style="font-weight:<%=word.equals("S")?"bold":"" %>">S</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('T');return false;" style="font-weight:<%=word.equals("T")?"bold":"" %>">T</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('U');return false;" style="font-weight:<%=word.equals("U")?"bold":"" %>">U</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('V');return false;" style="font-weight:<%=word.equals("V")?"bold":"" %>">V</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('W');return false;" style="font-weight:<%=word.equals("W")?"bold":"" %>">W</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('X');return false;" style="font-weight:<%=word.equals("X")?"bold":"" %>">X</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Y');return false;" style="font-weight:<%=word.equals("Y")?"bold":"" %>">Y</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Z');return false;" style="font-weight:<%=word.equals("Z")?"bold":"" %>">Z</a>
			</div>
		</td>
	</tr>
<%
	//apiKey - 농사로 Open API에서 신청 후 승인되면 확인 가능
	String apiKey="인증키를입력하세요";
	//서비스 명
	String serviceName="garden";
	//오퍼레이션 명	
	String[] operationName = {"lightList", "grwhstleList", "lefcolrList", "lefmrkList", "flclrList", "fmldecolrList", "ignSeasonList", "winterLwetList", "priceTypeList", "waterCycleList"};
	
	HashMap<String, Document> operationNameMap = new HashMap<String, Document>();
	
	Document doc = null;

	for(int i=0; i<operationName.length; i++){
		//XML 받을 URL 생성
		String parameter = "/"+serviceName+"/"+operationName[i];
		parameter += "?apiKey="+ apiKey;
		
		//서버와 통신
		URL apiUrl = new URL("http://api.nongsaro.go.kr/service"+parameter);
		InputStream apiStream = apiUrl.openStream();
		
		try{
			//xml document
			doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(apiStream);
			operationNameMap.put(operationName[i], doc);
		}catch(Exception e){
			e.printStackTrace();
		}finally{
			apiStream.close();
		}
	}
	
	int size = 0;
	String resultCode="";
	String resultMsg="";
	NodeList items = null;
	NodeList codes = null;
	NodeList codeNms = null;

	if(operationNameMap.containsKey("lightList")){
		doc=operationNameMap.get("lightList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>광도요구</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="lightChk" name="lightChk" value="<%=code%>" <%
				if(request.getParameter("lightChkVal") != null){
					String chkVar = request.getParameter("lightChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	if(operationNameMap.containsKey("grwhstleList")){
		doc=operationNameMap.get("grwhstleList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>생육형태</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="grwhstleChk" name="grwhstleChk" value="<%=code%>" <%
				if(request.getParameter("grwhstleChkVal") != null){
					String chkVar = request.getParameter("grwhstleChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//잎색 검색 조건
	if(operationNameMap.containsKey("lefcolrList")){
		doc=operationNameMap.get("lefcolrList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>잎색</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="lefcolrChk" name="lefcolrChk" value="<%=code%>" <%
				if(request.getParameter("lefcolrChkVal") != null){
					String chkVar = request.getParameter("lefcolrChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//잎무늬 검색 조건
	if(operationNameMap.containsKey("lefmrkList")){
		doc=operationNameMap.get("lefmrkList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>잎 무늬</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="lefmrkChk" name="lefmrkChk" value="<%=code%>" <%
				if(request.getParameter("lefmrkChkVal") != null){
					String chkVar = request.getParameter("lefmrkChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//꽃 색 검색 조건
	if(operationNameMap.containsKey("flclrList")){
		doc=operationNameMap.get("flclrList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>꽃색</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="flclrChk" name="flclrChk" value="<%=code%>" <%
				if(request.getParameter("flclrChkVal") != null){
					String chkVar = request.getParameter("flclrChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//열매색 검색 조건
	if(operationNameMap.containsKey("fmldecolrList")){
		doc=operationNameMap.get("fmldecolrList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>열매색</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="fmldecolrChk" name="fmldecolrChk" value="<%=code%>" <%
				if(request.getParameter("fmldecolrChkVal") != null){
					String chkVar = request.getParameter("fmldecolrChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//꽃피는 계절 검색 조건
	if(operationNameMap.containsKey("ignSeasonList")){
		doc=operationNameMap.get("ignSeasonList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();	
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>꽃피는 계절</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="ignSeasonChk" name="ignSeasonChk" value="<%=code%>" <%
				if(request.getParameter("ignSeasonChkVal") != null){
					String chkVar = request.getParameter("ignSeasonChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//겨울 최저온도 검색 조건
	if(operationNameMap.containsKey("winterLwetList")){
		doc=operationNameMap.get("winterLwetList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();	
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>겨울 최저온도</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
%>
				<input type="checkbox" id="winterLwetChk" name="winterLwetChk" value="<%=code%>" <%
				if(request.getParameter("winterLwetChkVal") != null){
					String chkVar = request.getParameter("winterLwetChkVal");
					String[] chkArr = chkVar.split(",");
					for(int j=0; j<chkArr.length; j++){
						if(code.equals(chkArr[j])){
							out.print("checked");
						}
					}
				}
				%> /><%=codeNm%>&nbsp;
<%
			}
			
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</td></tr>");
	}
	//가격대 검색 조건
	if(operationNameMap.containsKey("priceTypeList")){
		doc=operationNameMap.get("priceTypeList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();	
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>가격대</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
				if(i == 0){
%>
				<input type="radio" id="priceType" name="priceType" value="big" <%= priceType.equals("big") ? "checked": "" %>/>대형&nbsp;
				<input type="radio" id="priceType" name="priceType" value="medium" <%= priceType.equals("medium") ? "checked": "" %>/>중형&nbsp;
				<input type="radio" id="priceType" name="priceType" value="3" <%= priceType.equals("3") ? "checked": "" %>/>소형&nbsp;
				<select id="priceTypeSel" name="priceTypeSel">
				<option value="">선택하세요.</option>
<%
				}
%>
				<option value="<%=code%>" <%=priceTypeSel.equals(code)?"selected":""%>><%=codeNm%></option>
<%
			}
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</select></td></tr>");
	}
	//물주기 검색 조건
	if(operationNameMap.containsKey("waterCycleList")){
		doc=operationNameMap.get("waterCycleList");
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();	
		codes = doc.getElementsByTagName("code");
		codeNms = doc.getElementsByTagName("codeNm");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}
		
		out.print("<tr><th>물주기</th><td>");
		if(resultCode.equals("00")){
			for(int i=0; i<size; i++){
				//코드
				String code = codes.item(i).getFirstChild() == null ? "" : codes.item(i).getFirstChild().getNodeValue();
				//코드명
				String codeNm = codeNms.item(i).getFirstChild() == null ? "" : codeNms.item(i).getFirstChild().getNodeValue();
				if(i == 0){
%>
				<select id="waterCycleSel" name="waterCycleSel">
				<option value="">선택하세요.</option>
<%
				}
%>
				<option value="<%=code%>" <%=waterCycleSel.equals(code)?"selected":""%>><%=codeNm%></option>
<%
			}
		}else{
			out.print("조회한 정보가 없습니다.");
		}
		out.print("</select></td></tr>");
	}
%>
	</table>
</form>

<%
	//목록
	if(operationName.length == operationNameMap.size()){
		//오퍼레이션 명
		String operationNameList="gardenList";
		
		//XML 받을 URL 생성
		String parameter = "/"+serviceName+"/"+operationNameList;
		parameter += "?apiKey="+ apiKey;
		parameter += "&pageNo="+request.getParameter("pageNo");
		
		//검색 조건
		String[] searchNmArr = {"sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel"};
		for(int i=0; i<searchNmArr.length; i++){
			if(request.getParameter(searchNmArr[i])!=null && !request.getParameter(searchNmArr[i]).equals("")){
				parameter += "&"+searchNmArr[i]+"="+ request.getParameter(searchNmArr[i]);
			}
		}
		//서버와 통신
		URL apiUrl = new URL("http://api.nongsaro.go.kr/service"+parameter);
		InputStream apiStream = apiUrl.openStream();
		
		try{
			//xml document
			doc = DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(apiStream);
		}catch(Exception e){
			e.printStackTrace();
		}finally{
			apiStream.close();
		}
		
		items = doc.getElementsByTagName("item");
		size = doc.getElementsByTagName("item").getLength();
		NodeList cntntsNos = doc.getElementsByTagName("cntntsNo");
		NodeList cntntsSjs = doc.getElementsByTagName("cntntsSj");
		NodeList rtnFileSeCodes = doc.getElementsByTagName("rtnFileSeCode");
		NodeList rtnFileSns = doc.getElementsByTagName("rtnFileSn");
		NodeList rtnOrginlFileNms = doc.getElementsByTagName("rtnOrginlFileNm");
		NodeList rtnStreFileNms = doc.getElementsByTagName("rtnStreFileNm");
		NodeList rtnFileCourss = doc.getElementsByTagName("rtnFileCours");
		NodeList rtnImageDcs = doc.getElementsByTagName("rtnImageDc");
		NodeList rtnThumbFileNms = doc.getElementsByTagName("rtnThumbFileNm");
		NodeList rtnImgSeCodes = doc.getElementsByTagName("rtnImgSeCode");
		
		try{resultCode = doc.getElementsByTagName("resultCode").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultCode = "";}
		try{resultMsg = doc.getElementsByTagName("resultMsg").item(0).getFirstChild().getNodeValue();}catch(Exception e){resultMsg = "";}

		if(resultCode.equals("00")){ %>
		<hr>
		<table width="100%" border="1" cellSpacing="0" cellPadding="0">
<%
		if(size==0){
%>
			<tr>
				<td colspan="2" align="center">조회한 정보가 없습니다.</td>
			</tr>
<% 			
		}else{
			for(int i=0; i<size; i++){
				//콘텐츠 번호
				String cntntsNo = cntntsNos.item(i).getFirstChild() == null ? "" : cntntsNos.item(i).getFirstChild().getNodeValue();
				//콘텐츠 제목
				String cntntsSj = cntntsSjs.item(i).getFirstChild() == null ? "" : cntntsSjs.item(i).getFirstChild().getNodeValue();
				//저장 파일명
				String rtnStreFileNm = rtnStreFileNms.item(i).getFirstChild() == null ? "" : rtnStreFileNms.item(i).getFirstChild().getNodeValue();
				String[] rtnStreFileNmArr = rtnStreFileNm.split("[|]");
				//파일경로
				String rtnFileCours = rtnFileCourss.item(i).getFirstChild() == null ? "" : rtnFileCourss.item(i).getFirstChild().getNodeValue();
				String[] rtnFileCoursArr = rtnFileCours.split("[|]");
%>
			<tr>
			    <td width="15%"><img src="http://www.nongsaro.go.kr/<%=rtnFileCoursArr[0]%>/<%=rtnStreFileNmArr[0]%>" width="128" height="103"></img></td>
			    <td width="85%">
					<a href="javascript:fncDtl('<%=cntntsNo%>');"><%=cntntsSj%></a>
			    </td>
			</tr>
<%		
			}
		}
%>
	</table>
<%

	//페이징 처리
		//한 페이지에 제공할 건수
		String numOfRows = "";
		//조회된 총 건수
		String totalCount = "";
		//조회할 페이지 번호
		String pageNo = "";
		try{numOfRows = doc.getElementsByTagName("numOfRows").item(0).getFirstChild().getNodeValue();}catch(Exception e){numOfRows = "";}
		try{totalCount = doc.getElementsByTagName("totalCount").item(0).getFirstChild().getNodeValue();}catch(Exception e){totalCount = "";}
		try{pageNo = doc.getElementsByTagName("pageNo").item(0).getFirstChild().getNodeValue();}catch(Exception e){pageNo = "";}
	
		int pageGroupSize = 10;
		int pageSize = 0;
		try{
			pageSize = Integer.parseInt(numOfRows);
		}catch(Exception e){
			pageSize = 10;
		}
		int start = 0; 
		try{
			start = Integer.parseInt(pageNo);
		}catch(Exception e){
			start = 1;
		}
		
		int currentPage = 1;
		try{currentPage = Integer.parseInt(pageNo);}catch(Exception e){}
	
		int startRow = (currentPage - 1) * pageSize + 1;//한 페이지의 시작글 번호 
		int endRow = currentPage * pageSize;//한 페이지의 마지막 글번호      
		int count = Integer.parseInt(totalCount);                                                            
		int number=0;                                                             
			
		number=count-(currentPage-1)*pageSize;//글목록에 표시할 글번호                                                                  
	    
		//페이지그룹의 갯수                                                                                                             
		//ex) pageGroupSize가 3일 경우 '[1][2][3]'가 pageGroupCount 개 만큼 있다.                                                       
		int pageGroupCount = count/(pageSize*pageGroupSize)+( count % (pageSize*pageGroupSize) == 0 ? 0 : 1);                           
		//페이지 그룹 번호                                                                                                              
		//ex) pageGroupSize가 3일 경우  '[1][2][3]'의 페이지그룹번호는 1 이고  '[2][3][4]'의 페이지그룹번호는 2 이다.                   
		int numPageGroup = (int) Math.ceil((double)currentPage/pageGroupSize);                                                          
	
	
		if(count > 0){
			int pageCount = count / pageSize + ( count % pageSize == 0 ? 0 : 1);
			int startPage = pageGroupSize*(numPageGroup-1)+1;
			int endPage = startPage + pageGroupSize-1;
			int prtPageNo = 0;
			
			if(endPage > pageCount){
				endPage = pageCount;
			}
			
			if(numPageGroup > 1){
				prtPageNo = (numPageGroup-2)*pageGroupSize+1;
				out.println("<a href='javascript:fncGoPage("+prtPageNo+");'>[이전]</a>");
			}
			
			for(int i=startPage; i<=endPage; i++){
				prtPageNo = i;
				out.print("<a href='javascript:fncGoPage("+prtPageNo+");'>");
				if(currentPage == i){
					out.print("<strong>["+i+"]</strong>");
				}else{
					out.print("["+i+"]");
				}
				out.println("</a>");
			}
			
			if(numPageGroup < pageGroupCount){
				prtPageNo = (numPageGroup*pageGroupSize+1);
				out.println("<a href='javascript:fncGoPage("+prtPageNo+");'>[다음]</a>");
			}
		}
		//페이징 처리 끝
		}else{
			out.print(resultMsg);
		}
	}
%>
</body>
</html>