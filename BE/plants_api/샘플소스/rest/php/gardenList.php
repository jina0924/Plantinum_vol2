<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
?>


<html>
<head>
<meta http-dquiv="Content-Type" content="text/html" charset="utf-8">
<title>실내정원용 식물</title>
<script type='text/javascript'>
//상세보기
function fncDtl(cNo){
	with(document.searchApiForm){
		cntntsNo.value = cNo;
		method="get";
		action = "gardenDtl.php";
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
		action = "gardenList.php";
		target = "_self";
		submit();
	}
}
//페이지 이동
function fncGoPage(page){
	with(document.searchApiForm){
		pageNo.value = page;
		method="get";
		action = "gardenList.php";
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
<?PHP
$sType = isset($_REQUEST["sType"]) ? $_REQUEST["sType"] : "" ;
$wordType = isset($_REQUEST["wordType"]) ? $_REQUEST["wordType"] : "" ;
$word = isset($_REQUEST["word"]) ? $_REQUEST["word"] : "" ;
$priceType = isset($_REQUEST["priceType"]) ? $_REQUEST["priceType"] : "" ;
$priceTypeSel = isset($_REQUEST["priceTypeSel"]) ? $_REQUEST["priceTypeSel"] : "" ;
$waterCycleSel = isset($_REQUEST["waterCycleSel"]) ? $_REQUEST["waterCycleSel"] : "" ;
?>
<form name="searchApiForm">
<input type="hidden" name="cntntsNo">
<input type="hidden" name="pageNo" value="<?PHP if(isset($_REQUEST["pageNo"])){ echo $_REQUEST["pageNo"]; }?>">
<input type="hidden" name="word" value="<?PHP if(isset($_REQUEST["word"])){ echo $_REQUEST["word"]; }?>">
<input type="hidden" name="lightChkVal" value="<?PHP if(isset($_REQUEST["lightChkVal"])){ echo $_REQUEST["lightChkVal"]; }?>">
<input type="hidden" name="grwhstleChkVal" value="<?PHP if(isset($_REQUEST["grwhstleChkVal"])){ echo $_REQUEST["grwhstleChkVal"]; }?>">
<input type="hidden" name="lefcolrChkVal" value="<?PHP if(isset($_REQUEST["lefcolrChkVal"])){ echo $_REQUEST["lefcolrChkVal"]; }?>">
<input type="hidden" name="lefmrkChkVal" value="<?PHP if(isset($_REQUEST["lefmrkChkVal"])){ echo $_REQUEST["lefmrkChkVal"]; }?>">
<input type="hidden" name="flclrChkVal" value="<?PHP if(isset($_REQUEST["flclrChkVal"])){ echo $_REQUEST["flclrChkVal"]; }?>">
<input type="hidden" name="fmldecolrChkVal" value="<?PHP if(isset($_REQUEST["fmldecolrChkVal"])){ echo $_REQUEST["fmldecolrChkVal"]; }?>">
<input type="hidden" name="ignSeasonChkVal" value="<?PHP if(isset($_REQUEST["ignSeasonChkVal"])){ echo $_REQUEST["ignSeasonChkVal"]; }?>">
<input type="hidden" name="winterLwetChkVal" value="<?PHP if(isset($_REQUEST["winterLwetChkVal"])){ echo $_REQUEST["winterLwetChkVal"]; }?>">

<table width="100%" border="1" cellSpacing="0" cellPadding="0">
	<colgroup>
		<col width="20%"/>
		<col width="80%"/>
	</colgroup>
	<tr>
		<th>
			<select name="sType">
				<option value="sCntntsSj" <?= $sType=="sCntntsSj"?"selected":"" ?>>식물명</option>
				<option value="sPlntbneNm" <?= $sType=="sPlntbneNm"?"selected":"" ?>>한명</option>
				<option value="sPlntzrNm" <?= $sType=="sPlntzrNm"?"selected":"" ?>>영명</option>
			</select>
		</th>
		<td>
			<input type="text" name="sText" value="<?PHP if(isset($_REQUEST["sText"])){ echo $_REQUEST["sText"]; }?>">
			<input type="button" name="search" value="검색" onclick="return fncSearch();"/>
		</td>
	</tr>
	<tr>
		<th>
			<select id="wordType" name="wordType" onchange="javascript:fncWordTypeOption(); return false;">
				<option value="cntntsSj" <?= $wordType=="cntntsSj"?"selected":"" ?>>국명</option>
				<option value="plntbneNm" <?= $wordType=="plntbneNm"?"selected":"" ?>>학명</option>
			</select>
		</th>
		<td>
			<div id="koreanSrch" style="display: <?= $wordType=="" ? "block" : $wordType=="cntntsSj" ? "block" : "none" ?>;">
        <a href="#" onclick="javascript:fncContSearch('ㄱ');return false;" style="font-weight:<?= $word=="ㄱ"?"bold":"" ?>">ㄱ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄴ');return false;" style="font-weight:<?= $word=="ㄴ"?"bold":"" ?>">ㄴ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄷ');return false;" style="font-weight:<?= $word=="ㄷ"?"bold":"" ?>">ㄷ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㄹ');return false;" style="font-weight:<?= $word=="ㄹ"?"bold":"" ?>">ㄹ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅁ');return false;" style="font-weight:<?= $word=="ㅁ"?"bold":"" ?>">ㅁ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅂ');return false;" style="font-weight:<?= $word=="ㅂ"?"bold":"" ?>">ㅂ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅅ');return false;" style="font-weight:<?= $word=="ㅅ"?"bold":"" ?>">ㅅ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅇ');return false;" style="font-weight:<?= $word=="ㅇ"?"bold":"" ?>">ㅇ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅈ');return false;" style="font-weight:<?= $word=="ㅈ"?"bold":"" ?>">ㅈ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅊ');return false;" style="font-weight:<?= $word=="ㅊ"?"bold":"" ?>">ㅊ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅋ');return false;" style="font-weight:<?= $word=="ㅋ"?"bold":"" ?>">ㅋ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅌ');return false;" style="font-weight:<?= $word=="ㅌ"?"bold":"" ?>">ㅌ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅍ');return false;" style="font-weight:<?= $word=="ㅍ"?"bold":"" ?>">ㅍ</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('ㅎ');return false;" style="font-weight:<?= $word=="ㅎ"?"bold":"" ?>">ㅎ</a>
			</div>
			<div id="englishSrch" style="display: <?= $wordType=="plntbneNm"?"block":"none" ?>;">
				<a href="#" onclick="javascript:fncContSearch('A');return false;" style="font-weight:<?= $word=="A"?"bold":"" ?>">A</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('B');return false;" style="font-weight:<?= $word=="B"?"bold":"" ?>">B</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('C');return false;" style="font-weight:<?= $word=="C"?"bold":"" ?>">C</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('D');return false;" style="font-weight:<?= $word=="D"?"bold":"" ?>">D</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('E');return false;" style="font-weight:<?= $word=="E"?"bold":"" ?>">E</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('F');return false;" style="font-weight:<?= $word=="F"?"bold":"" ?>">F</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('G');return false;" style="font-weight:<?= $word=="G"?"bold":"" ?>">G</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('H');return false;" style="font-weight:<?= $word=="H"?"bold":"" ?>">H</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('I');return false;" style="font-weight:<?= $word=="I"?"bold":"" ?>">I</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('J');return false;" style="font-weight:<?= $word=="J"?"bold":"" ?>">J</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('K');return false;" style="font-weight:<?= $word=="K"?"bold":"" ?>">K</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('L');return false;" style="font-weight:<?= $word=="L"?"bold":"" ?>">L</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('M');return false;" style="font-weight:<?= $word=="M"?"bold":"" ?>">M</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('N');return false;" style="font-weight:<?= $word=="N"?"bold":"" ?>">N</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('O');return false;" style="font-weight:<?= $word=="O"?"bold":"" ?>">O</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('P');return false;" style="font-weight:<?= $word=="P"?"bold":"" ?>">P</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Q');return false;" style="font-weight:<?= $word=="Q"?"bold":"" ?>">Q</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('R');return false;" style="font-weight:<?= $word=="R"?"bold":"" ?>">R</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('S');return false;" style="font-weight:<?= $word=="S"?"bold":"" ?>">S</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('T');return false;" style="font-weight:<?= $word=="T"?"bold":"" ?>">T</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('U');return false;" style="font-weight:<?= $word=="U"?"bold":"" ?>">U</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('V');return false;" style="font-weight:<?= $word=="V"?"bold":"" ?>">V</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('W');return false;" style="font-weight:<?= $word=="W"?"bold":"" ?>">W</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('X');return false;" style="font-weight:<?= $word=="X"?"bold":"" ?>">X</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Y');return false;" style="font-weight:<?= $word=="Y"?"bold":"" ?>">Y</a>&nbsp;
				<a href="#" onclick="javascript:fncContSearch('Z');return false;" style="font-weight:<?= $word=="Z"?"bold":"" ?>">Z</a>
			</div>
		</td>
	</tr>

<?PHP
//apiKey - 농사로 Open API에서 신청 후 승인되면 확인 가능
$apiKey = "인증키를입력하세요";
//서비스 명
$serviceName = "garden";
//오퍼레이션 명
$operationName = array("lightList", "grwhstleList", "lefcolrList", "lefmrkList", "flclrList", "fmldecolrList", "ignSeasonList", "winterLwetList", "priceTypeList", "waterCycleList");

$urls = array();


for($i=0; $i<count($operationName); $i++){
  //XML 받을 URL 생성
  $parameter = "/".$serviceName."/".$operationName[$i];
  $parameter .= "?apiKey=".$apiKey;

  $url = "http://api.nongsaro.go.kr/service" . $parameter;

  $urls[$operationName[$i]] = $url;
}

$codes = "";
$codeNm = "";

//검색조건 명
$srchNmArr = array("광도요구", "생육형태", "잎색", "잎 무늬", "꽃 색", "열매 색", "꽃피는 계절", "겨울 최저온도", "가격대", "물주기");
//타입명
$typeNmArr = array("lightChk", "grwhstleChk", "lefcolrChk", "lefmrkChk", "flclrChk", "fmldecolrChk", "ignSeasonChk", "winterLwetChk", "priceTypeChk", "waterCycleChk");

for($i=0; $i<count($operationName); $i++){
  //오퍼레이션명
  $operNm = $operationName[$i];
	$srchNm = $srchNmArr[$i];
	$typeNm = $typeNmArr[$i];
	//타입명 값
	$typeVal = $typeNmArr[$i] ."Val";

  //XML Parsing
  $xml = file_get_contents($urls[$operationName[$i]]);
  //PHP5.x 이상이 설치되어 있어야 하며, php.ini에 allow_url_fopen을 on으로 해주시기 바랍니다.
  $object = simplexml_load_string($xml);

  echo "<tr><th>" .$srchNm ."</th><td>";
	if(count($object->body[0]->items[0]->item) == 0){
	echo "조회한 정보가 없습니다.";
	}else{
    $index = 0;
		foreach($object->body[0]->items[0]->item as $item){
			//코드
			$code = $item->code;
			//코드명
			$codeNm = $item->codeNm;

      if($operNm == "priceTypeList"){
        if($index == 0){
?>
        <input type="radio" id="priceType" name="priceType" value="big" <?= $priceType == "big" ? "checked" : "" ?> />대형&nbsp;
        <input type="radio" id="priceType" name="priceType" value="medium" <?= $priceType == "medium" ? "checked" : "" ?> />중형&nbsp;
        <input type="radio" id="priceType" name="priceType" value="3" <?= $priceType == "3" ? "checked" : "" ?> />소형&nbsp;
        <select id="priceTypeSel" name="priceTypeSel">
        <option value="">선택하세요.</option>
<?PHP
        }
?>
        <option value="<?=$code?>" <?= $priceTypeSel == $code ? "selected" : "" ?> ><?=$codeNm?></option>
<?PHP
      }else if ($operNm == "waterCycleList"){
        if($index == 0){
?>
        <select id="waterCycleSel" name="waterCycleSel">
        <option value="">선택하세요.</option>
<?PHP
        }
?>
        <option value="<?=$code?>" <?= $waterCycleSel == $code ? "selected" : "" ?> ><?=$codeNm?></option>
<?PHP
      }else{
?>
        <input type="checkbox" id="<?=$typeNm?>" name="<?=$typeNm?>" value="<?=$code?>" <?PHP
        if(isset($_REQUEST[$typeVal])){
          $chkVar = $_REQUEST[$typeVal];
          $chkArr = explode(",", $chkVar);
          for($j=0; $j<sizeof($chkArr); $j++){
            if($code == $chkArr[$j]){
              echo "checked";
            }
          }
        }
        ?> /><?=$codeNm?>&nbsp;
<?PHP
      }
    $index = $index + 1;
		}
  }
  if($operNm =="priceTypeList" || $operNm =="waterCycleList"){
    echo "</select>";
  }
  echo "</td></tr>";
}
?>
</table>
</form>
<hr>
<?PHP
if(true){
	//오퍼레이션 명
	$operationName = "gardenList";

	//XML 받을 URL 생성
	$parameter = "/".$serviceName."/".$operationName;
	$parameter .= "?apiKey=".$apiKey;

  $srchNmArr = array("pageNo","sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel");

  for($i=0; $i<sizeof($srchNmArr); $i++){
    if(isset($_REQUEST[$srchNmArr[$i]])){
      $parameter .= "&".$srchNmArr[$i]."=".$_REQUEST[$srchNmArr[$i]];
    }
  }

	$url = "http://api.nongsaro.go.kr/service" . $parameter;

	//XML Parsing
	$xml = file_get_contents($url);
	//PHP5.x 이상이 설치되어 있어야 하며, php.ini에 allow_url_fopen을 on으로 해주시기 바랍니다.
	$object = simplexml_load_string($xml);

	if(count($object->body[0]->items[0]->item) == 0){
	   echo "조회한 정보가 없습니다.";
	}else{
?>
	<table width="100%" border="1" cellSpacing="0" cellPadding="0">
<?PHP
		foreach($object->body[0]->items[0]->item as $item){
			//컨텐츠번호
			$cntntsNo = $item->cntntsNo;
			//컨텐츠 제목
			$cntntsSj = $item->cntntsSj;
			//저장 파일명
			$rtnStreFileNm = $item->rtnStreFileNm;
			//파일 경로
			$rtnFileCours = $item->rtnFileCours;

			$rtnStreFileNmArr=explode('|',$rtnStreFileNm);
			$rtnFileCoursArr=explode('|',$rtnFileCours);

?>
    <tr>
				<td width="15%"><img src="http://www.nongsaro.go.kr/<?=$rtnFileCoursArr[0]?>/<?=$rtnStreFileNmArr[0]?>" width="128" height="103"></img></td>
				<td width="85%">
				<a href="javascript:fncDtl('<?=$cntntsNo?>');"><?=$cntntsSj?></a>
				</td>
		</tr>
<?PHP
		}
?>
	</table>
<?PHP
	}
//페이징 처리
	//한 페이지에 제공할 건수
	$numOfRows = $object->body[0]->items[0]->numOfRows;
	//조회된 총 건수
	$totalCount = $object->body[0]->items[0]->totalCount;
	//조회할 페이지 번호
	$pageNo = $object->body[0]->items[0]->pageNo;

	$pageGroupSize = 10;
	$pageSize = 0;

	$pageSize = (int)$numOfRows;
	if($pageSize==0) $pageSize=10;

	$start = (int)$pageNo;
	if($start==0)$start=1;

	$currentPage = (int)$pageNo;

	$startRow = ($currentPage -1) * $pageSize +1;//한 페이지의 시작글 번호
	$endRow = $currentPage * $pageSize;//한 페이지의 마지막 글번호

	$count = (int)$totalCount;
	$number=0;

	$number=$count-($currentPage-1)*$pageSize;//글목록에 표시할 글번호

	//페이지그룹의 갯수
	//ex) pageGroupSize가 3일 경우 '[1][2][3]'가 pageGroupCount 개 만큼 있다.
	$pageGroupCount = $count/($pageSize*$pageGroupSize);

	//페이지 그룹 번호
	//ex) pageGroupSize가 3일 경우  '[1][2][3]'의 페이지그룹번호는 1 이고  '[2][3][4]'의 페이지그룹번호는 2 이다.
	$numPageGroup = (int)ceil((double)$currentPage/$pageGroupSize);

	if($count > 0){
		$pageCount = $count / $pageSize + ( $count % $pageSize == 0 ? 0 : 1);
		$startPage = $pageGroupSize*($numPageGroup-1)+1;
		$endPage = $startPage + $pageGroupSize-1;
		$startPnt = 0;

		if($endPage > $pageCount){
			$endPage = $pageCount;
		}

		if($numPageGroup > 1){
			$startPnt = ($numPageGroup-2)*$pageGroupSize+1;
			echo "<a href='javascript:fncGoPage(".$startPnt.");'>[이전]</a>";
		}

		for($i=$startPage; $i<=$endPage; $i++){
			$startPnt = $i;
			echo "<a href='javascript:fncGoPage(".$startPnt.");'>";

			if($currentPage == $i){
				echo "<strong>[$i]</strong>";
			}else{
				echo "[$i]";
			}
			echo "</a>";
		}

		if($numPageGroup < $pageGroupCount){
			$startPnt = ($numPageGroup*$pageGroupSize+1);
			echo "<a href='javascript:fncGoPage(".$startPnt.");'>[다음]</a>";
		}
	}
//페이징 처리 끝
}
?>

</body>
</html>
