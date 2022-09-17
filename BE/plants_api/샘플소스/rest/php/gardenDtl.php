<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);
?>

<html>
<head>
<meta http-dquiv="Content-Type" content="text/html" charset="utf-8">
<title>실내정원용 식물</title>
</head>
<body>
<h4><strong> * 샘플화면은 디자인을 적용하지 않았으니, 개별 사이트의 스타일에 맞게 코딩하시기 바랍니다.</strong></h4>
<h3><strong>실내정원용 식물</strong></h3>
<hr>
<?PHP
	//apiKey - 농사로 Open API에서 신청 후 승인되면 확인 가능
	$apiKey = "인증키를입력하세요";
	//서비스 명
	$serviceName = "garden";
	//오퍼레이션 명
	$operationName = "gardenDtl";

	//XML 받을 URL 생성
	$parameter = "/".$serviceName."/".$operationName;
	$parameter .= "?apiKey=".$apiKey;

	if(isset($_REQUEST["cntntsNo"])){
		$parameter .= "&cntntsNo=";
		$parameter .= $_REQUEST["cntntsNo"];
	}

	$url = "http://api.nongsaro.go.kr/service" . $parameter;

	//XML Parsing
	$xml = file_get_contents($url);
	//PHP5.x 이상이 설치되어 있어야 하며, php.ini에 allow_url_fopen을 on으로 해주시기 바랍니다.
	$object = simplexml_load_string($xml);

	//컨텐츠번호
  $cntntsNo            = $object->body[0]->item[0]->cntntsNo;
  //식물학명
  $plntbneNm           = $object->body[0]->item[0]->plntbneNm;
  //식물 영명
  $plntzrNm            = $object->body[0]->item[0]->plntzrNm;
  //유통명
  $distbNm             = $object->body[0]->item[0]->distbNm;
  //과 명
  $fmlNm               = $object->body[0]->item[0]->fmlNm;
  //원산지명
  $orgplceInfo         = $object->body[0]->item[0]->orgplceInfo;
  //조언정보
  $adviseInfo          = $object->body[0]->item[0]->adviseInfo;
  //이미지 평가 링크 명
  $imageEvlLinkCours   = $object->body[0]->item[0]->imageEvlLinkCours;
  //성장 높이 정보
  $growthHgInfo        = $object->body[0]->item[0]->growthHgInfo;
  //성장 넓이 정보
  $growthAraInfo       = $object->body[0]->item[0]->growthAraInfo;
  //잎형태 정보
  $lefStleInfo         = $object->body[0]->item[0]->lefStleInfo;
  //냄새 코드
  $smellCode           = $object->body[0]->item[0]->smellCode;
  //독설 정보
  $toxctyInfo          = $object->body[0]->item[0]->toxctyInfo;
  //번식 시기
  $prpgtEraInfo        = $object->body[0]->item[0]->prpgtEraInfo;
  //기타시기 정보
  $etcEraInfo          = $object->body[0]->item[0]->etcEraInfo;
  //관리수준 코드
  $managelevelCode     = $object->body[0]->item[0]->managelevelCode;
  //성장속도 코드
  $grwtveCode          = $object->body[0]->item[0]->grwtveCode;
  //생육온도 코드
  $grwhTpCode          = $object->body[0]->item[0]->grwhTpCode;
  //겨울최저 온도 코드
  $winterLwetTpCode    = $object->body[0]->item[0]->winterLwetTpCode;
  //습도 코드
  $hdCode              = $object->body[0]->item[0]->hdCode;
  //비트 정보
  $frtlzrInfo          = $object->body[0]->item[0]->frtlzrInfo;
  //토양 정보
  $soilInfo            = $object->body[0]->item[0]->soilInfo;
  //물주기 봄 코드
  $watercycleSprngCode = $object->body[0]->item[0]->watercycleSprngCode;
  //물주기 여름 코드
  $watercycleSummerCode= $object->body[0]->item[0]->watercycleSummerCode;
  //물주기 가을 코드
  $watercycleAutumnCode= $object->body[0]->item[0]->watercycleAutumnCode;
  //물주기 겨울 코드
  $watercycleWinterCode= $object->body[0]->item[0]->watercycleWinterCode;
  //병충해 관리 정보
  $dlthtsManageInfo    = $object->body[0]->item[0]->dlthtsManageInfo;
  //특별관리 정보
  $speclmanageInfo     = $object->body[0]->item[0]->speclmanageInfo;
  //기능성 정보
  $fncltyInfo          = $object->body[0]->item[0]->fncltyInfo;
  //화분직경 대 정보
  $flpodmtBigInfo      = $object->body[0]->item[0]->flpodmtBigInfo;
  //화분직경 중 정보
  $flpodmtMddlInfo     = $object->body[0]->item[0]->flpodmtMddlInfo;
  //화분직경 소 정보
  $flpodmtSmallInfo    = $object->body[0]->item[0]->flpodmtSmallInfo;
  //가로 대 정보
  $widthBigInfo        = $object->body[0]->item[0]->widthBigInfo;
  //가로 중 정보
  $widthMddlInfo       = $object->body[0]->item[0]->widthMddlInfo;
  //가로 소 정보
  $widthSmallInfo      = $object->body[0]->item[0]->widthSmallInfo;
  //세로 대 정보
  $vrticlBigInfo       = $object->body[0]->item[0]->vrticlBigInfo;
  //세로 중 정보
  $vrticlMddlInfo      = $object->body[0]->item[0]->vrticlMddlInfo;
  //세로 소 정보
  $vrticlSmallInfo     = $object->body[0]->item[0]->vrticlSmallInfo;
  //높이 대 정보
  $hgBigInfo           = $object->body[0]->item[0]->hgBigInfo;
  //높이 중 정보
  $hgMddlInfo          = $object->body[0]->item[0]->hgMddlInfo;
  //높이 소 정보
  $hgSmallInfo         = $object->body[0]->item[0]->hgSmallInfo;
  //볼륨 대 정보
  $volmeBigInfo        = $object->body[0]->item[0]->volmeBigInfo;
  //볼륨 중 정보
  $volmeMddlInfo       = $object->body[0]->item[0]->volmeMddlInfo;
  //볼륨 소 정보
  $volmeSmallInfo      = $object->body[0]->item[0]->volmeSmallInfo;
  //가격 대 정보
  $pcBigInfo           = $object->body[0]->item[0]->pcBigInfo;
  //가격 중 정보
  $pcMddlInfo          = $object->body[0]->item[0]->pcMddlInfo;
  //가격 소 정보
  $pcSmallInfo         = $object->body[0]->item[0]->pcSmallInfo;
  //관리요구도 코드
  $managedemanddoCode  = $object->body[0]->item[0]->managedemanddoCode;

?>
<table  border="1" cellspacing="0" cellpadding="0">
  <colgroup>
    <col width="15%">
    <col width="*">
  </colgroup>
  <tr>
      <th>식물학명</th>
      <td><?=$plntbneNm?></td>
  </tr>
  <tr>
      <th>식물영명</th>
      <td><?=$plntzrNm?></td>
  </tr>
  <tr>
      <th>유통명</th>
      <td><?=$distbNm?></td>
  </tr>
  <tr>
      <th>과명</th>
      <td><?=$fmlNm?></td>
  </tr>
  <tr>
      <th>원산지 정보</th>
      <td><?=$orgplceInfo?></td>
  </tr>
  <tr>
      <th>조언 정보</th>
      <td><?=$adviseInfo?></td>
  </tr>
  <tr>
      <th>이미지 평가 링크 경로</th>
      <td><?=$imageEvlLinkCours?></td>
  </tr>
  <tr>
      <th>성장 높이 정보</th>
      <td><?=$growthHgInfo?></td>
  </tr>
  <tr>
      <th>성장 넓이 정보</th>
      <td><?=$growthAraInfo?></td>
  </tr>
  <tr>
      <th>잎 형태 정보</th>
      <td><?=$lefStleInfo?></td>
  </tr>
  <tr>
      <th>냄새 코드</th>
      <td><?=$smellCode?></td>
  </tr>
  <tr>
      <th>독성 정보</th>
      <td><?=$toxctyInfo?></td>
  </tr>
  <tr>
      <th>번식 시기 정보</th>
      <td><?=$prpgtEraInfo?></td>
  </tr>
  <tr>
      <th>기타 시기 정보</th>
      <td><?=$etcEraInfo?></td>
  </tr>
  <tr>
      <th>관리수준 코드</th>
      <td><?=$managelevelCode?></td>
  </tr>
  <tr>
      <th>생장속도 코드</th>
      <td><?=$grwtveCode?></td>
  </tr>
  <tr>
      <th>생육 온도 코드</th>
      <td><?=$grwhTpCode?></td>
  </tr>
  <tr>
      <th>겨울 최저 온도 코드</th>
      <td><?=$winterLwetTpCode?></td>
  </tr>
  <tr>
      <th>습도 코드</th>
      <td><?=$hdCode?></td>
  </tr>
  <tr>
      <th>비료 정보</th>
      <td><?=$frtlzrInfo?></td>
  </tr>
  <tr>
      <th>토양 정보</th>
      <td><?=$soilInfo?></td>
  </tr>
  <tr>
      <th>물주기 봄 코드</th>
      <td><?=$watercycleSprngCode?></td>
  </tr>
  <tr>
      <th>물주기 여름 코드</th>
      <td><?=$watercycleSummerCode?></td>
  </tr>
  <tr>
      <th>물주기 가을 코드</th>
      <td><?=$watercycleAutumnCode?></td>
  </tr>
  <tr>
      <th>물주기 겨울 코드</th>
      <td><?=$watercycleWinterCode?></td>
  </tr>
  <tr>
      <th>병충해 관리 정보</th>
      <td><?=$dlthtsManageInfo?></td>
  </tr>
  <tr>
      <th>특별관리 정보</th>
      <td><?=$speclmanageInfo?></td>
  </tr>
  <tr>
      <th>기능성 정보</th>
      <td><?=$fncltyInfo?></td>
  </tr>
  <tr>
      <th>화분직경 대 정보</th>
      <td><?=$flpodmtBigInfo?></td>
  </tr>
  <tr>
      <th>화분직경 중 정보</th>
      <td><?=$flpodmtMddlInfo?></td>
  </tr>
  <tr>
      <th>화분직경 소 정보</th>
      <td><?=$flpodmtSmallInfo?></td>
  </tr>
  <tr>
      <th>가로 대 정보</th>
      <td><?=$widthBigInfo?></td>
  </tr>
  <tr>
      <th>가로 중 정보</th>
      <td><?=$widthMddlInfo?></td>
  </tr>
  <tr>
      <th>가로 소 정보</th>
      <td><?=$widthSmallInfo?></td>
  </tr>
  <tr>
      <th>세로 대 정보</th>
      <td><?=$vrticlBigInfo?></td>
  </tr>
  <tr>
      <th>세로 중 정보</th>
      <td><?=$vrticlMddlInfo?></td>
  </tr>
  <tr>
      <th>세로 소 정보</th>
      <td><?=$vrticlSmallInfo?></td>
  </tr>
  <tr>
      <th>높이 대 정보</th>
      <td><?=$hgBigInfo?></td>
  </tr>
  <tr>
      <th>높이 중 정보</th>
      <td><?=$hgMddlInfo?></td>
  </tr>
  <tr>
      <th>높이 소 정보</th>
      <td><?=$hgSmallInfo?></td>
  </tr>
  <tr>
      <th>볼륨 대 정보</th>
      <td><?=$volmeBigInfo?></td>
  </tr>
  <tr>
      <th>볼륨 중 정보</th>
      <td><?=$volmeMddlInfo?></td>
  </tr>
  <tr>
      <th>볼륨 소 정보</th>
      <td><?=$volmeSmallInfo?></td>
  </tr>
  <tr>
      <th>가격 대 정보</th>
      <td><?=$pcBigInfo?></td>
  </tr>
  <tr>
      <th>가격 중 정보</th>
      <td><?=$pcMddlInfo?></td>
  </tr>
  <tr>
      <th>가격 소 정보</th>
      <td><?=$pcSmallInfo?></td>
  </tr>
  <tr>
      <th>관리요구도 코드</th>
      <td><?=$managedemanddoCode?></td>
  </tr>
</table>
<br>
<input type="button" onclick="javascript:fncList();" value="목록"/>
<form name="searchApiForm">
<?PHP

$srchNmArr = array("pageNo","sType", "sText", "wordType", "word", "lightChkVal", "grwhstleChkVal", "lefcolrChkVal", "lefmrkChkVal", "flclrChkVal", "fmldecolrChkVal", "ignSeasonChkVal", "winterLwetChkVal", "priceType", "priceTypeSel", "waterCycleSel");

for($i=0; $i<sizeof($srchNmArr); $i++){
  $reqVal = isset($_REQUEST[$srchNmArr[$i]]) ? $_REQUEST[$srchNmArr[$i]] : "";
  echo "<input type='hidden' name='" . $srchNmArr[$i] . "' value='" . $reqVal . "' />";
}

?>
</form>
<script type="text/javascript">
//목록이동
function fncList(){
	with(document.searchApiForm){
		method="get";
		action = "gardenList.php";
		target = "_self";
		submit();
	}
}
</script>
</body>
</html>
