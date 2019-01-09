from bs4 import BeautifulSoup
import lxml
html = '''<!DOCTYPE html>
<html>
<head>
<title>博客來-東京迪士尼遊園餐廳導覽指南2016～2017</title>
<meta charset="UTF-8">
<meta name="keywords" content="東京迪士尼遊園餐廳導覽指南2016～2017">
<meta name="description" content="東京迪士尼遊園餐廳導覽指南2016～2017">
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="博客來">
<meta name="format-detection" content="telephone=no">
<meta name="format-detection" content="address=no">
<meta property="og:site_name" content="博客來"/>
<meta property="og:type" content="product"/>
<meta property="fb:app_id" content="210743125726405" />
<meta property="og:title" content="東京迪士尼遊園餐廳導覽指南2016～2017"/>
<meta property="og:image" content="https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043.jpg&v=577ca56d&w=250&h=250"/>
<meta property="og:image:width" content="250">
<meta property="og:image:height" content="250">
<meta property="og:url" content="http://www.books.com.tw/products/M010053043" />
<meta property="og:description" content="東京迪士尼遊園餐廳導覽指南2016～2017"/>
<link rel="canonical" href="https://www.books.com.tw/products/M010053043">
<link rel="apple-touch-icon" href="//jci.book.com.tw/img/icons/apple_icon_120x120.png">
<link rel="apple-touch-icon" sizes="76x76" href="//jci.book.com.tw/img/icons/apple_icon_72x72.png">
<link rel="apple-touch-icon" sizes="120x120" href="//jci.book.com.tw/img/icons/apple_icon_120x120.png">
<link rel="apple-touch-icon" sizes="152x152" href="//jci.book.com.tw/img/icons/apple_icon_152x152.png">
<link href="//jci.book.com.tw/css/iconfont/icon_01.css" rel="stylesheet" type="text/css" media="all">
<link rel="stylesheet" type="text/css" media="all" href="/csss/mobile.css?v=5c2056c1">
<link href="//jci.book.com.tw/jss/books/mobilebase/css/mobile_base.css" rel="stylesheet" type="text/css" media="all" />
<link href="//jci.book.com.tw/jss/books/mobilebase/css/mobile_header.css" rel="stylesheet" type="text/css" media="all" />
<link href="//jci.book.com.tw/jss/books/mobilebase/css/mobile_tool.css" rel="stylesheet" type="text/css" media="all" />
<link href="//jci.book.com.tw/jss/slick/slick-1.8.1/slick/slick.css" rel="stylesheet" type="text/css" media="all">
<link href="//jci.book.com.tw/jss/slick/slick-1.8.1/slick/slick-theme.min.css" rel="stylesheet" type="text/css" media="all">
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-TBZGS7');</script><script>dataLayer.push({"ecommerce":{"detail":{"products":[{"id":"M010053043","name":"\u6771\u4eac\u8fea\u58eb\u5c3c\u904a\u5712\u9910\u5ef3\u5c0e\u89bd\u6307\u53572016\uff5e2017","price":90,"category":"M01"}]}}});</script>
<script  type="text/javascript" src="//jci.book.com.tw/jss/books/head.min.js"></script>
<script  type="text/javascript" src="//www.books.com.tw/jss/web/m_weblink.js?v=5b1dd0e2"></script>
<script type="text/javascript" src="//jci.book.com.tw/jss/jquery/jquery-1.11.1.min.js"></script>
<script type="text/javascript" src="//jci.book.com.tw/jss/slick/slick-1.8.1/slick/slick.js"></script>
</head>
<body>
<div id="M201106_0_getTakelook_P00e502810067_pop" class="mobile_takealook">
<div>
<span class="takealook_closebtn"><i class="icon-fail"></i></span>
<span class="takealook_loading"><i class="icon-spin6 animate-spin"></i></span>
<img>
</div></div><div id="filter_win" class="popup_win01">
<div class="popup_win01_content">
<header style="">
<span class="text">篩選</span>
<span class="closebtn"><i class="icon-cancel"></i></span>
</header>
<div class="popup_win01_content_scroll">
</div><div class="fbar">
<div class="buttons">
<a class="bt_gray cancel">取消</a>
<a class="bt_orange confirm">確認</a>
</div></div></div></div><div id="page" class="prod">
<div class="page-sidebar left">
<div class="page-sidebar-scroll">
<nav>
<ul id="all_cat" class="cat">
<li class="icon-right dark collapsed deep-0" data-catid="root_web">
<div>
<span>全站分類</span>
<span><i class="icon-down-open"></i><i class="icon-up-open"></i></span>
</div><ul></ul>
</li>
</ul>
<ul id="ovs_cat" class="cat">
<li class="icon-right dark collapsed deep-0" data-catid="root_ovs">
<div>
<span>海外專區</span>
<span><i class="icon-down-open"></i><i class="icon-up-open"></i></span>
</div><ul></ul>
</li>
</ul>
<ul class="onelevel"><li class="expanded"><div><span>天天最低價</span></div><ul><li><a href="https://www.books.com.tw/happybuy?loc=m_menu_0_001"><div>天天瘋狂BUY</div></a></li><li><a href="https://activity.books.com.tw/books66/?loc=m_menu_0_002"><div>今日66折</div></a></li><li><a href="https://www.books.com.tw/web/sys_todaydept?loc=m_menu_0_003"><div>每日一物</div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>排行榜</span></div><ul><li><a href="https://www.books.com.tw/web/sys_hourstop/home?loc=m_menu_1_001"><div>全館即時榜</div></a></li><li><a href="https://www.books.com.tw/web/sys_futureboard/home?loc=m_menu_1_002"><div>熱銷預購榜</div></a></li><li><a href="https://www.books.com.tw/web/sys_newtopb/books?loc=m_menu_1_003"><div>新書暢銷榜</div></a></li><li><a href="https://www.books.com.tw/web/sys_basesale/design?loc=m_menu_1_004"><div>家居生活暢銷榜</div></a></li><li><a href="https://www.books.com.tw/web/sys_basesale/stationery?loc=m_menu_1_005"><div>設計文具暢銷榜</div></a></li><li><a href="https://www.books.com.tw/web/sys_basesale/food?loc=m_menu_1_006"><div>美食暢銷榜</div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>電子書服務</span></div><ul><li><a href="https://viewer-ebook.books.com.tw/viewer/index.html?readlist=all&MemberLogout=true&loc=m_menu_2_001" target="_blank"><div><span>電子書櫃</span><span><i class="icon-link-ext"></i></span></div></a></li><li><a href="https://www.books.com.tw/activity/2017/05/ebooknewer/?loc=m_menu_2_002"><div><span>新手上路</span><span><i class="icon-link-ext"></i></span></div></a></li><li><a href="https://www.books.com.tw/activity/2017/08/ebkdownload/?loc=m_menu_2_003" target="_blank"><div><span>電子書App下載</span><span><i class="icon-link-ext"></i></span></div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>OKAPI</span></div><ul><li><a href="https://okapi.books.com.tw/category/8?loc=m_menu_3_001" target="_blank"><div>閱讀現場</div></a></li><li><a href="https://okapi.books.com.tw/category/27?loc=m_menu_3_002" target="_blank"><div>過生活</div></a></li><li><a href="https://okapi.books.com.tw/category/32?loc=m_menu_3_003" target="_blank"><div>一起讀</div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>福利專區</span></div><ul><li><a href="https://benefit.books.com.tw/drawer/login?loc=m_menu_4_001" target="_blank"><div>電子禮物卡兌換</div></a></li><li><a href="https://benefit.books.com.tw/drawer_card/login?loc=m_menu_4_002" target="_blank"><div>實體禮物卡兌換</div></a></li><li><a href="https://www.books.com.tw/benefit/?loc=m_menu_4_003" target="_blank"><div>福利專區介紹</div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>更多優質服務</span></div><ul><li><a href="javascript:void(0);" class="mobile_open_app"><div><span>下載博客來快找APP</span><span><i class="icon-link-ext"></i></span></div></a></li><li><a href="https://tickets.books.com.tw/index/?loc=m_menu_5_002" target="_blank"><div><span>售票網</span><span><i class="icon-desktop"></i></span></div></a></li><li><a href="javascript:void(0);" class="mobile_lang_open"><div><span><i class="icon-globe"></i></span><span>繁體中文</span></div></a></li><li><a href="javascript:void(0);" class="mobile_to_pc"><div><span>前往博客來電腦版</span><span><i class="icon-desktop"></i></span></div></a></li></ul></li></ul><ul class="onelevel"><li class="expanded"><div><span>與我們聯絡</span></div><ul><li><a href="https://www.books.com.tw/web/csservice?loc=m_menu_6_001"><div>線上客服</div></a></li></ul></li></ul></nav></div>
</div><div class="page-sidebar right" >
<div class="page-sidebar-scroll">
<div id="member">
<div class="login-block">
<div class="section member-name">
<a href="https://myaccount.books.com.tw/myaccount/myaccount/getRecord?loc=m_tw_header_record">
<div>
<span id="member_title" class="member_text">
<img src="//jci.book.com.tw/img/member/member_s.svg" alt="一般會員" />
<span></span>您好      </span>
<span><i class="icon-right-open"></i></span>
</div></a>
</div><div class="section list">
<div><a href="https://myaccount.books.com.tw/myaccount/myaccount/m_MemberDiscount?loc=m_member_001"><div><span>本月獨享優惠</span></div></a></div><div><a href="https://www.books.com.tw/bank?loc=m_member_002"><div><span>銀行優惠</span></div></a></div><div><a href="https://www.books.com.tw/myaccount/getNextBuy?loc=m_member_003"><div><span>下次再買清單</span></div></a></div><div><a href="https://www.books.com.tw/web/sys_browseitems?loc=m_member_004"><div><span>瀏覽紀錄</span></div></a></div></div>
<ul class="onelevel">
<li>
<div><span>交易紀錄</span></div>
<ul><li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getOrder?loc=m_tw_header_order"><div><span>訂單查詢</span></div></a></li><li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getOrderTicket?loc=m_tw_header_order_ticket"><div><span>售票網訂單</span></div></a></li><li id="software_order_li" style="display:none"><a href="https://myaccount.books.com.tw/myaccount/myaccount/getOrderSerial?loc=m_header_order_software"><div><span>下載版序號專區</span></div></a></li></ul>
</li>
</ul>
<ul class="onelevel">
<li>
<div><span>優惠 / 帳戶餘額</span></div>
<ul class="accountlist">
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getShoppingmoneylist?loc=m_tw_header_account_001"><div><span>可用購物金</span><span class="number" id="shopping_cash">0</span><span>點</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getPercentcouponlist?loc=m_tw_header_account_002"><div><span>可用E-Coupon</span><span class="number" id="my_ecoupon_count">0</span><span>張</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getPercentIcouponlist?loc=m_tw_header_account_003"><div><span>可用單品折價券</span><span class="number" id="my_icoupon_count">0</span><span>張</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getBalance?loc=m_tw_header_account_004"><div><span>帳戶餘額</span><span class="number" id="cash">0</span><span>元</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getFreemoneylist?loc=m_tw_header_account_005"><div><span>可用儲值金</span><span class="number" id="benefit_cash">0</span><span>元</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getOpenpointlist?loc=m_tw_header_account_006"><div><span>OPENPOINT</span></div></a></li>
</ul>
</li>
</ul>
<ul class="onelevel collapsible">
<li class="collapsed">
<div>
<span>信件備份</span>
<span><i class="icon-down-open"></i><i class="icon-up-open"></i></span>
</div><ul>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getSystemMail?loc=m_tw_header_mail_box"><div><span>系統信件備份</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/getCallCenterMail?loc=m_tw_header_mail_qa"><div><span>客服中心回函</span></div></a></li>
</ul>
</li>
</ul>
<ul class="onelevel collapsible">
<li class="collapsed">
<div>
<span>會員資料</span>
<span><i class="icon-down-open"></i><i class="icon-up-open"></i></span>
</div><ul>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/modifyMemberinfo?loc=m_tw_header_memberinfo"><div><span>修改會員資料</span></div></a></li>
<li><a href="https://myaccount.books.com.tw/myaccount/myaccount/changePassword?loc=m_tw_header_change_psd"><div><span>修改密碼</span></div></a></li>
</ul>
</li>
</ul>
<div class="section">
<a href="https://myaccount.books.com.tw/myaccount/myaccount?loc=m_tw_header_myaccount"><div><span>會員專區</span><span><i class="icon-desktop"></i></span></div></a>
</div><div class="section">
<a href="https://cart.books.com.tw/member/logout?loc=m_tw_header_logout"><div><span><i class="icon-log-out"></i></span><span>登出</span></div></a>
</div></div></div>
</div></div><div class="page-sidebar right" >
<div class="page-sidebar-scroll">
<div id="custom">
</div></div></div><div class="page-content">
<link rel="stylesheet" type="text/css" href="//jci.book.com.tw/css/iconfont/icon_01.css" media="all">
<div class="overlay" style="display:none;opacity:1 z-index:99999999" id="div_language_win" >
<div class="alert_win aligner-box">
<div class="multi-language-dlg">
<span class="pop_closebtn"><i class="icon-fail" onclick="B.$('#div_language_win').style.display ='none';"></i></span>
<h4>選擇語言</h4>
<ul>
<li ><a class="btn" href="javascript:;" onclick="change_lang('en');">English</a></li>
<li  class="here"><a class="btn" href="javascript:;" onclick="change_lang('zh_TW');">繁體中文</a></li>
<li ><a class="btn" href="javascript:;" onclick="change_lang('zh_CN');">简体中文</a></li>
</ul>
</div></div></div><div id="header" class="mod clearfix">
<span id="open-navi"><i class="icon-menu"></i></span>
<span id="open-search"><i class="icon-search"></i></span>
<span id="logo" data-href="//www.books.com.tw?loc=m_tw_header_logo" title="回博客來">
<img src="//jci.book.com.tw/img/logo/mainlogo_02.svg" alt="博客來">
</span>
<span id="open-cart" data-href="https://db.books.com.tw/shopping/cart_list.php?loc=m_tw_header_cart"><i class="icon-basket"></i><strong id="shopping_cart_num">0</strong></span>
<span id="open-member"><i class="icon-user"></i></span>
</div><div id="searchbox">
<div class="content">
<form action="https://search.books.com.tw/search/query/" name="search" id="search" method="GET" >
<select name="cat" class="icon-user">
<option value="all">全部</option>
<option value="BKA">圖書</option>
<option value="EBA">電子書</option>
<option value="AVA">影音</option>
<option value="DPA">百貨</option>
<option value="MGA">雜誌</option>
<option value="TKA">售票</option>
<option value="OVS">海外專館</option>
</select>
<div class="keyword">
<input type="text" accesskey="S" list="search_words" name="key" id="key" value="" message="請輸入關鍵字" autocomplete="off" placeholder="請輸入關鍵字">
<button type="submit" title="搜尋"><i class="icon-search"></i></button>
<datalist id="search_words"></datalist>
<ul id="search_words_ul" style="display: none;"></ul>
</div></form>
<div class="keyword_list">
<section class="box">
<h3>熱門關鍵字</h3>
<div><a href="https://search.books.com.tw/search/query/key/%E6%98%9F%E5%B7%B4%E5%85%8B%20%E8%B1%AC/spell/1/fclick/hotkey">星巴克 豬</a><a href="https://search.books.com.tw/search/query/key/%E7%84%A1%E5%8D%B0%E8%89%AF%E5%93%81/spell/1/fclick/hotkey">無印良品</a><a href="https://search.books.com.tw/search/query/key/%E4%BA%94%E6%9C%88%E5%A4%A9/spell/1/fclick/hotkey">五月天</a><a href="https://search.books.com.tw/search/query/key/%E5%94%90%E7%B6%BA%E9%99%BD/spell/1/fclick/hotkey">唐綺陽</a><a href="https://search.books.com.tw/search/query/key/%E6%98%9F%E5%B7%B4%E5%85%8B/spell/1/fclick/hotkey">星巴克</a><a href="https://search.books.com.tw/search/query/key/%E8%94%A1%E5%BA%B7%E6%B0%B8/spell/1/fclick/hotkey">蔡康永</a><a href="https://search.books.com.tw/search/query/key/%E7%A6%8F%E8%A2%8B/spell/1/fclick/hotkey">福袋</a><a href="https://search.books.com.tw/search/query/key/%E7%B4%85%E5%8C%85%E8%A2%8B/spell/1/fclick/hotkey">紅包袋</a><a href="https://search.books.com.tw/search/query/key/%E7%8E%8B%E5%AE%8F%E5%93%B2/spell/1/fclick/hotkey">王宏哲</a><a href="https://search.books.com.tw/search/query/key/%E6%9B%BE%E4%B9%8B%E5%96%AC/spell/1/fclick/hotkey">曾之喬</a></div>
</section>
<section class="box">
<h3>您最近找過</h3>
<div id="search_history"></div>
</section>
</div></div></div><div id="content">
<div class="maskdiv"></div>
<script type="text/javascript">
$(document).ready(function(){
    var click_open_breadcrumb = new weblink('open-breadcrumb');
});
</script>
<input type="hidden" id="menu_breadcrumb" value="M010901">
<div class="m_mod mm_013 clearfix">
<h1 itemprop="name">東京迪士尼遊園餐廳導覽指南2016～2017</h1>
<h2><a href='https://search.books.com.tw/search/query/cat/all/key/%E6%9D%B1%E4%BA%AC%E3%83%87%E3%82%A3%E3%82%BA%E3%83%8B%E3%83%BC%E3%83%AA%E3%82%BE%E3%83%BC%E3%83%88%E3%83%AC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%B3%E3%82%AC%E3%82%A4%E3%83%89%E3%83%96%E3%83%83%E3%82%AF%202016%EF%BC%8D2017'>東京ディズニーリゾートレストランガイドブック 2016－2017</a></h2>
</div><div class="m_mod mm_014 clearfix" id="M201106_0_getTakelook_P00e502810067">
<div class="m_scrollable" div style="">
<div class="slider_wrap">
<ul>
<li class="current">
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043.jpg&v=577ca56d&w=250&h=250" >
</li><li>
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_bc_01.jpg&v=577ca56d&w=250&h=250" >
</li><li>
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_01.jpg&v=57b296cf&w=250&h=250" >
</li><li>
<img  class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_12.jpg&v=57b296cf&w=250&h=250" >
</li><li>
<img  class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_18.jpg&v=57b296cf&w=250&h=250" >
</li><li>
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_19.jpg&v=57b296cf&w=250&h=250" >
</li><li>
<img  class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_20.jpg&v=57b296cf&w=250&h=250" >
</li><li>
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_53.jpg&v=57b296d0&w=250&h=250" >
</li><li>
<img  class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_82.jpg&v=57b296d0&w=250&h=250" >
</li><li>
<img  class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_93.jpg&v=57b296d0&w=250&h=250" >
</li><li>
<img  class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_98.jpg&v=57b296d0&w=250&h=250" >
</li>
</ul>
</div></div></div><div class="m_mod mm_016 clearfix">
<ul>
<li><a href="https://www.books.com.tw/web/mook">MOOK</a>><a href="https://www.books.com.tw/web/mook_topm_09/">生活情報</a>><a href="https://www.books.com.tw/web/sys_mkbotm/mook/0901/">旅遊情報</a></li>
</ul>
</div><div class="m_mod mm_016 clearfix">
<ul>
<li><span class="title">出版地區：</span>日本                                            </li><li><span class="title">出版日期：</span>2016/07/01</li>
<li><span class="title">語言：</span>日文                                            </li><li><span class="title">上架日期：</span>2016/07/16</li>
</ul>
</div><div id="M201105_0_getMgProdInfo_P00e502810069" style="display:none;"></div><div class="overlay" style="display:none;opacity:1 z-index:99999999" id="trace_box">
<div class="alert_win aligner-box">
<div class="m016_alert_win">
<table>
<thead>
<tr>
<th>請勾選欲追蹤的作者</th>
</tr>
</thead>
<tbody id="list_trace"></tbody>
</table>
<div class="button_wrap clearfix">
<a href="javascript:saveTrace();" class="button">確定</a>
<a href="javascript:cancelTrace();" class="button cancel">取消</a>
</div></div></div></div><script>
$(window).load(function(){
    setFollow('',':'); //class name , author : pubid
});
function setFollow(c,ap){
    var opt_module_id = 'M201105_0_getMgProdInfo_P00e502810069'; //模組編碼參數
    var opt = new Array(3); //參數資料變數
    opt[0] = c; //class name
    opt[1] = new Array(3);
    opt[1][0] = 'M010053043:M201105_0_getMgProdInfo_P00e502810069:M201502_007_view'; //item : li_id : view
    opt[1][1] = ap; //author : pubid
    opt[1][2] = window.location.href; //url
    opt[1][3] = 'M'; //device_source
    opt[2] = 'M201502_007_view' //template
    var M201105_0_getMgProdInfo_P00e502810069 = new ajax_product_show(opt_module_id,opt);
}
        
function saveTrace(){
    var author='';
    $('input[name="author"]:checked:enabled').each(function(index){
         author += ((index===0)?'':',') + $(this).val();
    });
    setFollow('setFollowAuthorAjax', author);
    $('#trace_box').hide();
}
function cancelTrace(){
    $('#trace_box').hide();
}
 function editTrace(url){
    window.open(url, '_blank');
    $('#trace_box').hide();
}
</script>
<div class="m_mod mm_017 clearfix">
<ul>
<li class="price">
<span><em>2</em>折</span>$<b>90</b></li>
</ul>
</div><div class="m_mod mm_019 clearfix">
<p>分享</p>
<ul class="icon-push">
<li id="push_facebook" class="icon-fb"><a href="#" title="分享到Facebook"><span>分享到Facebook</span></a></li>
<li id="push_line" class="icon-line"><a href="#" title="用LINE傳送"><span>用LINE傳送</span></a></li>
</ul>
</div><div class="m_mod mm_032 clearfix">
<ul>
<h3 class="title03">促銷合購</h3>
<li><a href="https://www.books.com.tw/web/exhibition/">2019國際書展3折起，滿1000元現折100元！</a></li></ul>
</div><div class="m_mod mm_020 clearfix">
<h2>運送方式</h2>
<ul>
<li><i class="icon-1"></i><span>可配送點：</span>台灣、蘭嶼、綠島、澎湖、金門、馬祖、全球</li><li><i class="icon-2"></i><span>可取貨點：</span>台灣、蘭嶼、綠島、澎湖、金門、馬祖、香港、澳門、新加坡、馬來西亞</li>
</ul>
</div><div class="m_mod mm_023 clearfix more_on_off_M201105_0_getProdTextInfo_P00e502810072">
<a name="CategoryP00e502810072"></a>
<h2>編者的話</h2>
<article>
<section class="more_off" id="M201105_0_getProdTextInfo_P00e502810072_h1"><span style="color:#ff0000;"><strong>東京迪士尼海洋15</strong><strong>週年特別MENU</strong><strong>大特集＆餐廳資訊</strong></span><br />
<br />
進入迪士尼樂園與海洋，彷彿就像進到一個夢幻國度一樣。不只擁有許多好玩的設施，賣許多迪士尼角色周邊商品的店，還有與迪士尼角色結合的系列餐廳都是大家的關注重點所在。還要扣除排隊的時間，遊玩的時間就這麼少，當然要把握黃金的一分一秒，在事先做充分的資訊收集。這本東京迪士尼遊園餐廳導覽指南2016～2017，提供給你各式各樣東京迪士尼度假區餐廳的資訊。<br />
 <br />
幾乎和開園時同時營業的餐廳、擁有許多座位的餐廳…等等，首先為大家帶來東京迪士尼餐廳基本情報。為了慶祝15週年，就連餐廳也摩拳擦掌，推出各式各樣的特別MENU，這裡透過東京迪士尼海洋15週年特別MENU大特集將這些珍貴資訊帶給你。當然還有分成東京迪士尼樂園與海洋來分別介紹各區域的餐廳資訊，就連周邊飯店的餐廳資訊也有帶來給你喔！</section>
<div class="more" style="display:block;">
<a href="javascript:;" class="M201105_0_getProdTextInfo_P00e502810072 ctl_more_on" id="M201105_0_getProdTextInfo_P00e502810072_m1"><i class="icon-down-open"></i>看更多</a>
</div></article>
</div><div class="m_mod mm_034 clearfix">
<h2>內頁簡介</h2>
<a href="javascript:;" title="往前" id="prev_M201101_0_getExcerptData_P00e502810073" style="display:hidden"><i class="icon-left-hand"></i></a>
<div class="box" id="box_M201101_0_getExcerptData_P00e502810073">
<ul id="page_intro_M201101_0_getExcerptData_P00e502810073">
<li class="item">
<h4>P.1 【夾頁附錄】東京迪士尼樂園＆海洋餐廳地圖</h4>
<div class="clearfix">
<img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_01.jpg&v=57b296cf&w=135&h=135&q=" alt="【夾頁附錄】東京迪士尼樂園＆海洋餐廳地圖" />
<blockquote>
<p>夾頁附錄為大家帶來的是東京迪士尼樂園＆海洋餐廳地圖，讓你率先掌握鎖定餐館的所在之處。</p>
</blockquote>
</div></li><li class="item">
<h4>P.12 東京迪士尼度假區情報</h4>
<div class="clearfix">
<img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_12.jpg&v=57b296cf&w=135&h=135&q=" alt="東京迪士尼度假區情報" />
<blockquote>
<p>購買票券的種類與價錢、交通方式&hellip;等等，首先為大家帶來的是東京迪士尼度假區基本情報。</p>
</blockquote>
</div></li><li class="item">
<h4>P.18 東京迪士尼餐廳基本情報</h4>
<div class="clearfix">
<img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_18.jpg&v=57b296cf&w=135&h=135&q=" alt="東京迪士尼餐廳基本情報" />
<blockquote>
<p>幾乎和開園時同時營業的餐廳、擁有許多座位的餐廳&hellip;等等，這裡為大家帶來東京迪士尼餐廳基本情報。</p>
</blockquote>
</div></li><li class="item">
<h4>P.19 東京迪士尼餐廳最新NEWS</h4>
<div class="clearfix">
<img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_19.jpg&v=57b296cf&w=135&h=135&q=" alt="東京迪士尼餐廳最新NEWS" />
<blockquote>
<p>不只設施，迪士尼餐廳也隨著時代更新，這裡為大家帶來2015年夏天到2016年春天的更新情報。</p>
</blockquote>
</div></li><li class="item">
<h4>P.20 東京迪士尼海洋15週年特別MENU大特集</h4>
<div class="clearfix">
<img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_20.jpg&v=57b296cf&w=135&h=135&q=" alt="東京迪士尼海洋15週年特別MENU大特集" />
<blockquote>
<p>為了慶祝15週年，從豪華料理到各種角色新菜單都有推出，這裡為大家帶來東京迪士尼海洋15週年特別MENU大特集。</p>
</blockquote>
</div></li><li class="item">
<h4>P.53 東京迪士尼海洋－失落河三角洲餐廳</h4>
<div class="clearfix">
<img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_53.jpg&v=57b296d0&w=135&h=135&q=" alt="東京迪士尼海洋－失落河三角洲餐廳" />
<blockquote>
<p>想吃到美味的墨西哥料理嗎？那就一定要來東京迪士尼海洋的失落河三角洲的餐廳嘗鮮。</p>
</blockquote>
</div></li><li class="item">
<h4>P.82 表演秀餐廳</h4>
<div class="clearfix">
<img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_82.jpg&v=57b296d0&w=135&h=135&q=" alt="表演秀餐廳" />
<blockquote>
<p>一邊吃飯，一邊還可以觀賞玩具總動員胡迪與翠絲等等角色的演出！？這裡為大家介紹這間採事前預約制的表演秀餐廳。</p>
</blockquote>
</div></li><li class="item">
<h4>P.93 東京迪士尼樂園－明日樂園餐廳</h4>
<div class="clearfix">
<img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_93.jpg&v=57b296d0&w=135&h=135&q=" alt="東京迪士尼樂園－明日樂園餐廳" />
<blockquote>
<p>玩具總動員三眼怪甜點、米奇手套漢堡&hellip;等等，介紹明日樂園餐廳裡面的美食。</p>
</blockquote>
</div></li><li class="item">
<h4>P.98 東京迪士尼度假區周邊飯店餐廳</h4>
<div class="clearfix">
<img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/005/30/M010053043_b_98.jpg&v=57b296d0&w=135&h=135&q=" alt="東京迪士尼度假區周邊飯店餐廳" />
<blockquote>
<p>除了介紹遊園區裡面的餐廳之外，也為大家介紹四間東京迪士尼度假區周邊飯店的餐廳資訊。</p>
</blockquote>
</div></li>
</ul>
</div><a href="javascript:;" title="往後" id="next_M201101_0_getExcerptData_P00e502810073"><i class="icon-right-hand"></i></a>
</div><div class="mm_024 clearfix">
<h2>
<a name="P00e502810074">
<strong>詳細資料</strong>
<i class="icon-down-open"></i>
</a>
</h2>
<section style="display:none" id="hide_or_show_M201101_0_getMgProdDetailInfo_P00e502810074" class="hide">
<ul><li>條碼：9784063505276</li><li>規格：平裝                                             / 104頁 / 26 x 21 cm / 普通級                                          / 全彩印刷                                      </li></ul>
<ul class="sort">
<li>本書分類：生活情報&gt; <a href='https://www.books.com.tw/web/sys_mkbotm/mook/0901/'>旅遊情報</a></li>
</ul>
</section>
</div><div class="mm_018 clearfix">
<h2>
<a>購物說明
<i class="icon-down-open"></i>
</a>
</h2>
<section style="display:none" id="hide_or_show_M201101_0_getShoppingInfo_P00e502810077" class="hide">
<p><strong><font color="#000080">到貨時間說明</font></strong><span style="white-space: normal; word-spacing: 0px; text-transform: none; float: none; color: rgb(38,38,38); text-align: justify; font: 13px/22px Arial, Helvetica, sans-serif, 新細明體; display: inline !important; letter-spacing: normal; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px"><span class="Apple-converted-space">&nbsp;</span></span></p>
<p>1.新刊預購：於預購期間內訂購，請參考商品頁的預計到貨日(此為首批商品到貨日期)，若您於預購期間內訂購但逾期未到貨，則是因為您訂購時已超過首批到貨量，需再向日本加訂，到貨時間約是原預計到貨日後3~4週，如有特殊情況將在商品頁中說明，請讀者以博客來寄出的取貨通知信件為準。</p>
<p>2.既刊調貨：既刊商品為商品頁僅顯示上架日期無預計到貨日，訂購該類且無庫存之商品，在您完成訂單程序之後，調貨時間約7~14個工作日左右，但若台灣供應商已無庫存，需由日本再進口，則時間約需3~4週，如有特殊情況將在商品頁中說明，請讀者以博客來寄出的取貨通知信件為準。</p>
<p>&nbsp;</p>
<p><span style="line-height: 1.6em; font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify; color: rgb(254, 40, 40);"><strong>退換貨說明</strong></span><span style="color: rgb(38, 38, 38); text-align: justify; line-height: 22px; font-family: Arial, Helvetica, sans-serif, 新細明體; font-stretch: normal;">&nbsp;</span></p>
<p><span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">請注意！下列商品購買後博客來不提供10天的猶豫期，請務必詳閱商品說明並再次確認確有購買該項商品之需求及意願時始下單購買，有任何疑問並請先聯繫博客來客服詢問：&nbsp;</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">1.易於腐敗、保存期限較短或解約時即將逾期。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">2.客製化之商品。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">3.報紙、期刊或雜誌。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">4.經消費者拆封之影音商品或電腦軟體。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">5.下載版軟體、資訊及電子書。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">6.涉及個人衛生，並經消費者拆封之商品，如：內衣褲、刮鬍刀&hellip;等。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">7.藝文展覽票券、藝文表演票券。</span><br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<br style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;" />
<span style="color: rgb(38, 38, 38); font-family: Arial, Helvetica, sans-serif, PMingLiU; text-align: justify;">非屬上列品項之商品均享有到貨十天的猶豫期﹝含例假日﹞。退回之商品必須於猶豫期內寄回。&nbsp;</span><br />
<br />
<b style="font-size: 13px; font-family: Arial, Helvetica, sans-serif, 新細明體; font-variant: normal; white-space: normal; word-spacing: 0px; text-transform: none; color: rgb(38,38,38); font-style: normal; text-align: justify; letter-spacing: normal; line-height: 22px; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px">辦理退換貨時，商品必須是全新狀態與完整包裝(請注意保持商品本體、配件、贈品、保證書、原廠包裝及所有附隨文件或資料的完整性，切勿缺漏任何配件或損毀原廠外盒)。退回商品無法回復原狀者，恐將影響退貨權益或需負擔部分費用。</b><span style="white-space: normal; word-spacing: 0px; text-transform: none; float: none; color: rgb(38,38,38); text-align: justify; font: 13px/22px Arial, Helvetica, sans-serif, 新細明體; display: inline !important; letter-spacing: normal; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px"><span class="Apple-converted-space">&nbsp;</span></span><br style="white-space: normal; word-spacing: 0px; text-transform: none; color: rgb(38,38,38); text-align: justify; font: 13px/22px Arial, Helvetica, sans-serif, 新細明體; letter-spacing: normal; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px" />
<br style="white-space: normal; word-spacing: 0px; text-transform: none; color: rgb(38,38,38); text-align: justify; font: 13px/22px Arial, Helvetica, sans-serif, 新細明體; letter-spacing: normal; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px" />
<b style="font-size: 13px; font-family: Arial, Helvetica, sans-serif, 新細明體; font-variant: normal; white-space: normal; word-spacing: 0px; text-transform: none; color: rgb(38,38,38); font-style: normal; text-align: justify; letter-spacing: normal; line-height: 22px; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px">訂購本商品前請務必詳閱商品<a href="https://www.books.com.tw/web/sys_qalist/qa_36_87/0?loc=000_087" style="text-decoration: underline; color: rgb(51,51,51); outline-width: medium; outline-style: none; outline-color: invert">退換貨原則</a>。</b><span style="white-space: normal; word-spacing: 0px; text-transform: none; float: none; color: rgb(38,38,38); text-align: justify; font: 13px/22px Arial, Helvetica, sans-serif, 新細明體; display: inline !important; letter-spacing: normal; background-color: rgb(255,255,255); text-indent: 0px; -webkit-text-stroke-width: 0px"><span class="Apple-converted-space">&nbsp;</span></span></p>
</section>
</div><div class="m_mod mm_027 clearfix">
<h2><strong>本類暢銷榜</strong></h2>
<div class="m_scrollable">
<ul class="m_scrollable_wrap">
<li id="li_M201101_0_getMagTopBoardList_P00e502810075-0" class="item">
<div class="img_wrap">
<a  href="https://www.books.com.tw/products/M010083407?loc=M_018_0_101"><span class="rank">1</span><img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/008/34/M010083407.jpg&v=5bfd0eee&w=140&h=140" alt="優質生活俱樂部特別號（2018.12）：附史努比提袋＆料理月曆" />
</a>
</div><div class="info">
<h4><a  href="https://www.books.com.tw/products/M010083407?loc=M_018_0_201">優質生活俱樂部特別號（2018.12）：附史努比提袋＆料理月曆</a></h4>
<p class="price">$<b>310</b></p>
</div></li><li id="li_M201101_0_getMagTopBoardList_P00e502810075-1" class="item">
<div class="img_wrap">
<a  href="https://www.books.com.tw/products/M010084599?loc=M_018_0_102"><span class="rank">2</span><img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/008/45/M010084599.jpg&v=5c1869bd&w=140&h=140" alt="Casa BRUTUS日本全國溫泉150完全專集" />
</a>
</div><div class="info">
<h4><a  href="https://www.books.com.tw/products/M010084599?loc=M_018_0_202">Casa BRUTUS日本全國溫泉150完全專集</a></h4>
<p class="price">$<b>660</b></p>
</div></li><li id="li_M201101_0_getMagTopBoardList_P00e502810075-2" class="item">
<div class="img_wrap">
<a  href="https://www.books.com.tw/products/M010070708?loc=M_018_0_103"><span class="rank">3</span><img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/007/07/M010070708.jpg&v=5ab4bb0a&w=140&h=140" alt="BRUTUS特別編集 台灣特集" />
</a>
</div><div class="info">
<h4><a  href="https://www.books.com.tw/products/M010070708?loc=M_018_0_203">BRUTUS特別編集 台灣特集</a></h4>
<p class="price"><span>9折</span>$<b>286</b></p>
</div></li><li id="li_M201101_0_getMagTopBoardList_P00e502810075-3" class="item">
<div class="img_wrap">
<a  href="https://www.books.com.tw/products/M010082817?loc=M_018_0_104"><span class="rank">4</span><img class="cover" src="//im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/008/28/M010082817.jpg&v=5beb88ba&w=140&h=140" alt="Hanako TRIP旅遊情報完全特集：台灣。" />
</a>
</div><div class="info">
<h4><a  href="https://www.books.com.tw/products/M010082817?loc=M_018_0_204">Hanako TRIP旅遊情報完全特集：台灣。</a></h4>
<p class="price"><span>9折</span>$<b>348</b></p>
</div></li><li id="li_M201101_0_getMagTopBoardList_P00e502810075-4" class="item">
<div class="img_wrap">
<a  href="https://www.books.com.tw/products/M010084600?loc=M_018_0_105"><span class="rank">5</span><img class="cover" src="//im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/M01/008/46/M010084600.jpg&v=5c1869bd&w=140&h=140" alt="LOVE！最愛刺蝟完全特刊：附刺蝟造型收納包" />
</a>
</div><div class="info">
<h4><a  href="https://www.books.com.tw/products/M010084600?loc=M_018_0_205">LOVE！最愛刺蝟完全特刊：附刺蝟造型收納包</a></h4>
<p class="price">$<b>770</b></p>
</div></li>
</ul>
</div></div><div class="m_mod mm_060 clearfix">
<h3>相關活動</h3>
<ul>
<li>
<a href="https://activity.books.com.tw/crosscat/show/A00000003354">
<img alt="1/1~2/18 限定 ∥ 我的旅行Packing list 嚴選旅用品5折起" src="//im1.book.com.tw/image/getImage?i=https://addons.books.com.tw/G/ADbanner/lifestyle/M/2019/01/packing_414.jpg&v=5c208449&w=414&h=208">
</a>
</li></ul>
</div><script type="application/ld+json">{
"@context": "http://schema.org/",
"@type": "SaleEvent",
"url": "https://activity.books.com.tw/crosscat/show/A00000003354",
"image": "https://im1.book.com.tw/image/getImage?i=https://addons.books.com.tw/G/ADbanner/lifestyle/M/2019/01/packing_414.jpg&v=5c208449&w=414&h=208",
"name": "1/1~2/18 限定 ∥ 我的旅行Packing list 嚴選旅用品5折起",
"description": "1/1~2/18 限定 ∥ 我的旅行Packing list 嚴選旅用品5折起",
"startDate": "2019-01-01 00:00:00.0",
"endDate": "2019-02-18 23:59:59.0",
"location": {
    "@type": "Place",
    "name": "博客來",
    "address": {
        "@type": "Text"
        }
    }
}
</script><div class="m_mod mm_011 clearfix">
<script type='text/javascript'>
  var googletag = googletag || {};
  googletag.cmd = googletag.cmd || [];
  (function() {
    var gads = document.createElement('script');
    gads.async = true;
    gads.type = 'text/javascript';
    var useSSL = 'https:' == document.location.protocol;
    gads.src = (useSSL ? 'https:' : 'http:') +
      '//www.googletagservices.com/tag/js/gpt.js';
    var node = document.getElementsByTagName('script')[0];
    node.parentNode.insertBefore(gads, node);
  })();
</script>
<script type='text/javascript'>
  googletag.cmd.push(function() {
    googletag.defineSlot('/17812066/books_books_M_320x100_bot', [320, 100], 'div-gpt-ad-1463731644737-0').addService(googletag.pubads());
    googletag.pubads().enableSingleRequest();
    googletag.pubads().collapseEmptyDivs();
    googletag.enableServices();
  });
</script>
<div id='div-gpt-ad-1463731644737-0'>
<script type='text/javascript'>
googletag.cmd.push(function() { googletag.display('div-gpt-ad-1463731644737-0'); });
</script>
</div></div></div><div id="footer">
<div>
<a href="//www.books.com.tw/?loc=m_tw_footer_home">首頁</a><a href="https://db.books.com.tw/shopping/cart_list.php?loc=m_tw_footer_cart">購物車</a><a href="https://myaccount.books.com.tw/myaccount/myaccount?loc=m_tw_footer_myaccount" target="_blank">會員專區<i class="icon-desktop"></i></a>
</div><div>
<span>檢視 :</span>行動版<a href="javascript:void(0);" class="mobile_to_pc">電腦版<i class="icon-desktop"></i></a>
</div><hr>
<div class="info">
<a href="//www.books.com.tw/services/privacy.htm?loc=m_tw_footer_inprivacy" target="_blank">資訊安全</a><a href="//www.books.com.tw/services/privacy.htm?loc=m_tw_footer_privacy" target="_blank">隱私權政策</a><a href="//www.books.com.tw/data/qanda/servicepolicy.htm?loc=m_tw_footer_servicepolicy" target="_blank">會員條款</a>
</div><div class="copyright">©博客來數位科技股份有限公司</div>
</div></div></div><div class="fixed-element">
<div class="m_tool mt_001" style="display: flex">
<i class="icon-up-1"></i>
</div></div><div class="m_fixed ms_001 clearfix" style="z-index: 9999" id='M201105_0_getProdCartInfo_P00e502810066'>
載入中...
</div><script language="JavaScript" type="text/javascript" src="/jss/web/product.js"></script>
<script type="text/javascript">
//$(document).ready(function(){
$(window).load(function(){
  getProdShoppingCartBtn();
});
function getProdShoppingCartBtn(){
    var opt_module_id = "M201105_0_getProdCartInfo_P00e502810066";//模組編碼參數
    var opt = new Array(3);//參數資料變數
    opt[1] = new Array();
    opt[0] = "getProdCartInfoAjax";//class name
    opt[1][0] = "M010053043";//item   
    opt[2] = "M201502_032_view"//template
    var M201105_0_getProdCartInfo_P00e502810066 = new ajax_product_show(opt_module_id,opt);
}
</script>
<script>
    head.load([
        "//jci.book.com.tw/jss/books/lazyload/blazy.min.js",
        "//jci.book.com.tw/jss/books/mobilebase/js/mobile_base.js",
        "//jci.book.com.tw/jss/books/mobilebase/js/mobile_header.js",
        "//jci.book.com.tw/jss/books/mobilebase/js/mobile_tool.js",
        "//www.books.com.tw/jss/web/adv_log.js?v=5aefea69",
        "//www.books.com.tw/jss/jquery/plugin/jquery.timers-1.2.js?v=593f57ff","//www.books.com.tw/jss/web/m_takealook_window.js?v=5af4ff18","//www.books.com.tw/jss/web/share_to_fb.js?v=593f57ff","//www.books.com.tw/jss/web/ajax_product_show.js?v=5ba9d569","//www.books.com.tw/jss/web/m_more_on_off.js?v=593f57ff","//www.books.com.tw/jss/web/m_hide_or_show.js?v=5ab0cbfc","//www.books.com.tw/jss/web/m_switch_slide_prod.js?v=593f57ff","//www.books.com.tw/jss/web/m_show_more.js?v=593f57ff","//www.books.com.tw/jss/web/m_switch_page.js?v=593f57ff"],
    function(){
    /*------------模組JS 1------------*/
        (function(){
            B.header.init({},"v20150701");
            (function(){
 var opt_module_id_c = "M201106_0_getTakelook_P00e502810067";//模組編碼參數
 var opt_module_id_p = "M201106_0_getTakelook_P00e502810067_pop";//模組編碼參數
 var M201106_0_getTakelook_P00e502810067 = new mobile_takealook_window(opt_module_id_c,opt_module_id_p);
})();
(function(){
    var fb = new share_to_fb();
})();
(function(){
   var opt_module_id = "M201105_0_getProdTextInfo_P00e502810072";//模組編碼參數
   var opt_element_id = "P00e502810072";  
   var M201105_0_getProdTextInfo_P00e502810072 = new more_on_off(opt_module_id,opt_element_id);
})();
(function(){
 var opt_module_id = "M201101_0_getExcerptData_P00e502810073";//模組編碼參數
 var M201101_0_getExcerptData_P00e502810073 = new switch_slide_prod(opt_module_id);
})();
(function(){
 var opt_module_id = "M201101_0_getMgProdDetailInfo_P00e502810074";//模組編碼參數
 var M201101_0_getMgProdDetailInfo_P00e502810074 = new hide_or_show(opt_module_id);
})();
(function(){
 var opt_module_id = "M201101_0_getShoppingInfo_P00e502810077";//模組編碼參數
 var M201101_0_getShoppingInfo_P00e502810077 = new hide_or_show(opt_module_id);
})();
        })();
    });
</script>
</body>
</html>'''

bs = BeautifulSoup(html,'lxml')

