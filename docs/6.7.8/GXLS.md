<p>描述主要和重要更新内容。</p>
<span class="anchor" id="4dbb5209-87bc-4290-853a-43535f8181b2"></span>
## 1.版本
<p><strong>v2024.12.4</strong></p>
<span class="anchor" id="92fe6769-cd19-469c-9ac1-b19c6581fdc1"></span>
## 2.更新历史
<ul>
<li><p>2024/12/4</p>
<ol>
<li>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERACTION/">ReqExecOrderAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEACTION/">ReqQuoteAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEACTION/">ReqOptionSelfCloseAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQBATCHORDERACTION/">ReqBatchOrderAction</a>中InvestorID字段为必填项</li>
</ol></li>
<li><p>2024/11/30</p>
<ol>
<li><p>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYDEPTHMARKETDATA/">ReqQryDepthMarketData</a>字段ProductClass（产品类型）为可以作为过滤字段</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORINFOCOMMREC/">ReqQryInvestorInfoCommRec</a>添加接口说明</p></li>
</ol></li>
<li><p>2024/11/22</p>
<ol>
<li><p>新增<a href="../QTYWGZ/TGATE/">TGate网关接入指南</a></p></li>
<li><p>更新版本6.7.8，具体说明见<a href="../6.7.8BBGXSM/">6.7.8版本更新说明</a></p></li>
<li><p>新增接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORINFOCOMMREC/">ReqQryInvestorInfoCommRec</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORINFOCOMMREC/">OnRspQryInvestorInfoCommRec</a></p></li>
<li><p>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/GETFRONTINFO/">GetFrontInfo</a>字段说明（查询频率-&gt;查询流控、FTD频率-&gt;FTD流控）</p></li>
<li><p>增加<a href="../HQJK/CTHOSTFTDCMDSPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>返回字段内容LoginDRIdentityID（当前登录中心号）、UserDRIdentityID（用户所属中心号）</p></li>
</ol></li>
<li><p>2024/10/17</p>
<ol>
<li>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-05">ReqOrderInsert</a>中CombOffsetFlag的字段说明</li>
</ol></li>
<li><p>2024/9/6</p>
<ol>
<li><p>更新版本6.7.7，具体说明见<a href="../6.7.7BBGXSM/">6.7.7版本更新说明</a></p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERINSERT/">OnRspOrderInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNORDERINSERT/">OnErrRtnOrderInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYORDER/">OnRspQryOrder</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERACTION/">OnRspOrderAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNORDERACTION/">OnErrRtnOrderAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQUOTEINSERT/">OnRspQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNQUOTEINSERT/">OnErrRtnQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQUOTEACTION/">OnRspQuoteAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEACTION/">ReqQuoteAction</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYQUOTE/">OnRspQryQuote</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNQUOTEACTION/">OnErrRtnQuoteAction</a>新增OrderMemo（报单回显字段）、SessionReqSeq（session上请求计数 api自动维护）字段</p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYDEPTHMARKETDATA/">ReqQryDepthMarketData</a>新增ProductClass（产品类型）字段</p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFMARGINRATIO/">OnRspQryInvestorPortfMarginRatio</a>新增ProductGroupID（产品群代码）字段</p></li>
<li><p>新增接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/GETFRONTINFO/">GetFrontInfo</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFSETTING/">ReqQryInvestorPortfSetting</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFSETTING/">OnRspQryInvestorPortfSetting</a></p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODRCAMSMARGIN/">OnRspQryInvestorProdRCAMSMargin</a>中CloseCombFrozenMargin、CloseFrozenMargin注释调整</p></li>
</ol></li>
<li><p>2024/9/5</p>
<ol>
<li>调整<a href="../QTYWGZ/HQSM.html#anchor-id-01">各交易所行情区别</a>说明，郑商所七期行情不再支持4Tick/秒，仅有2Tick/秒</li>
</ol></li>
<li><p>2024/8/16</p>
<ol>
<li>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/SUBSCRIBEPRIVATETOPIC/">SubscribePrivateTopic</a>说明，不订阅也会按照restart模式运行。</li>
</ol></li>
<li><p>2024/7/9</p>
<ol>
<li><p><a href="../QTYWGZ/TJDGZ/">条件单规则</a>中增加字段说明和5个使用场景实例。</p></li>
<li><p>由于中金所新增期货期权，在<a href="../QTYWGZ/QHQQDHQ-ZDCGZ/">期货期权的行权、自对冲</a>中更新对中金所行权的描述。</p></li>
</ol></li>
<li><p>2024/6/12</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTCOMMISSIONRATE.html#anchor-id-01">ReqQryInstrumentCommissionRate</a>中新增接口返回结果faq，看结果是交易所的还是投资者手续费率</li>
</ol></li>
<li><p>2024/6/4</p>
<ol>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITIONCOMBINEDETAIL.html#anchor-id-01">ReqQryInvestorPositionCombineDetail</a>添加关于rule组保开启后查不到持仓的说明。</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE.html#anchor-id-11">OnRtnTrade</a>增加faq关于成交价来源的说明</p></li>
</ol></li>
<li><p>2024/5/30</p>
<ol>
<li><p><a href="../QTYWGZ/BJHXJ/">做市商询价和报价</a>中关于中金所是否支持撤销单边衍生单调整为不支持。</p></li>
<li><p>新增页面<a href="../QTYWGZ/HQLK/">行情流控</a></p></li>
</ol></li>
<li><p>2024/5/20</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERSPI/REGISTERUSERSYSTEMINFO.html#anchor-id-01">RegisterUserSystemInfo</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/SUBMITUSERSYSTEMINFO.html#anchor-id-01">SubmitUserSystemInfo</a>中添加-7报错</li>
</ol></li>
<li><p>2024/4/18</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL.html#anchor-id-02">OnRspQryInvestorPositionDetail</a>调整字段PositionProfitByTrade关于大商所rule的说明。</li>
</ol></li>
<li><p>2024/4/8</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERSPI/REQPARKEDORDERINSERT.html#anchor-id-01">ReqParkedOrderInsert</a>中添加faq后台版本672开始不支持报入预埋条件单、预埋预埋单。</li>
</ol></li>
<li><p>2024/3/28</p>
<ol>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYORDER.html#anchor-id-01">OnRspQryOrder</a>增加OrderSource、ActiveTraderID、ActiveUserID的说明</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER.html#anchor-id-03">OnRtnOrder</a>补充OrderSource、ActiveTraderID、ActiveUserID的说明</p></li>
</ol></li>
<li><p>2024/3/15</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTDISCONNECTED.html#anchor-id-01">OnFrontDisconnected</a>调整断线返回代码注解</li>
</ol></li>
<li><p>2024/3/6</p>
<ol>
<li><a href="../JYJK/CTHOSTFTDCTRADERSPI/CREATEFTDCTRADERAPI.html#anchor-id-01">CreateFtdcTraderApi</a>添加faq。</li>
</ol></li>
<li><p>2024/2/20</p>
<ol>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a>修订成交金额turnover的说明。</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>修订持仓成本和持仓成本差值的说明</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRISKSETTLEINVSTPOSITION/">OnRspQryRiskSettleInvstPosition</a>修订持仓成本差值的说明</p></li>
<li><p><a href="../QTYWGZ/DCEZB/">大商所组保</a>修订持仓成本和持仓成本差值的说明</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL.html#anchor-id-01">OnRspQryInvestorPositionDetail</a>中添加volume字段说明</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>和<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYORDER/">OnRspQryOrder</a>修订撤销时间CancelTime的字段说明</p></li>
</ol></li>
<li><p>2024/1/9</p>
<ol>
<li><p>行情和交易的登录接口IPAddress字段说明调整</p></li>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYDEPTHMARKETDATA/">OnRspQryDepthMarketData</a>中Turnover的说明</p></li>
</ol></li>
<li><p>2024/1/2</p>
<ol>
<li>增加<a href="../6.7.2BBGXSM/">6.7.2版本更新说明</a>中关于心跳机制的调整说明</li>
</ol></li>
<li><p>2023/11/7</p>
<ol>
<li>更新<a href="../QTYWGZ/QHQQDHQ-ZDCGZ.html#anchor-id-02">期货期权的行权、自对冲</a>中撤销自动行权和自对冲指令的方式，由于6.7.2支持撤销其他席位发起的“取消到期自动行权”指令或“期权自对冲”指令</li>
</ol></li>
<li><p>2023/10/28</p>
<ol>
<li><p>更新版本6.7.2，具体说明见<a href="../6.7.2BBGXSM/">6.7.2版本更新说明</a></p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a>新增AddOnLockRateX2（期货合约内部对锁仓附加费率折扣比例）字段</p></li>
<li><p>接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a>新增AddOnIntraRateY2（品种内合约间对锁仓附加费率折扣比例）字段</p></li>
<li><p>新增接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMADDONINTERPARAMETER/">ReqQrySPBMAddOnInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSCOMBPRODUCTINFO/">ReqQryRCAMSCombProductInfo</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSINSTRPARAMETER/">ReqQryRCAMSInstrParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTRAPARAMETER/">ReqQryRCAMSIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTERPARAMETER/">ReqQryRCAMSInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSSHORTOPTADJUSTPARAM/">ReqQryRCAMSShortOptAdjustParam</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRCAMSINVESTORCOMBPOSITION/">ReqQryRCAMSInvestorCombPosition</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRCAMSMARGIN/">ReqQryInvestorProdRCAMSMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRULEINSTRPARAMETER/">ReqQryRULEInstrParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRULEINTRAPARAMETER/">ReqQryRULEIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYRULEINTERPARAMETER/">ReqQryRULEInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODRULEMARGIN/">ReqQryInvestorProdRULEMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMADDONINTERPARAMETER/">OnRspQrySPBMAddOnInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSCOMBPRODUCTINFO/">OnRspQryRCAMSCombProductInfo</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINSTRPARAMETER/">OnRspQryRCAMSInstrParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTRAPARAMETER/">OnRspQryRCAMSIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINTERPARAMETER/">OnRspQryRCAMSInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSSHORTOPTADJUSTPARAM/">OnRspQryRCAMSShortOptAdjustParam</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINVESTORCOMBPOSITION/">OnRspQryRCAMSInvestorCombPosition</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODRCAMSMARGIN/">OnRspQryInvestorProdRCAMSMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINSTRPARAMETER/">OnRspQryRULEInstrParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTRAPARAMETER/">OnRspQryRULEIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTERPARAMETER/">OnRspQryRULEInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODRULEMARGIN/">OnRspQryInvestorProdRULEMargin</a></p></li>
</ol></li>
<li><p>2023/10/17</p>
<ol>
<li>增加[<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL/">OnRspQryInvestorPositionDetail</a>]和[<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>]中SettlementPrice字段的说明</li>
</ol></li>
<li><p>2023/10/11</p>
<ol>
<li>修订<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRCOMMRATE.html#anchor-id-02">ReqQryOptionInstrCommRate</a>中的示例</li>
</ol></li>
<li><p>2023/9/26</p>
<ol>
<li><p>更新版本6.7.1，具体说明见<a href="../6.7.1BBGXSM/">6.7.1版本更新说明</a></p></li>
<li><p>新增<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORCOMMODITYSPMMMARGIN/">ReqQryInvestorCommoditySPMMMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORCOMMODITYGROUPSPMMMARGIN/">ReqQryInvestorCommodityGroupSPMMMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPMMINSTPARAM/">ReqQrySPMMInstParam</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPMMPRODUCTPARAM/">ReqQrySPMMProductParam</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYSPMMMARGIN/">OnRspQryInvestorCommoditySPMMMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYGROUPSPMMMARGIN/">OnRspQryInvestorCommodityGroupSPMMMargin</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMINSTPARAM/">OnRspQrySPMMInstParam</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMPRODUCTPARAM/">OnRspQrySPMMProductParam</a></p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQUOTEINSERT/">OnRspQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNQUOTEINSERT/">OnErrRtnQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUOTEINSERT/">ReqQuoteInsert</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYQUOTE/">OnRspQryQuote</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNQUOTE/">OnRtnQuote</a>接口结构体中增加TimeCondition（有效期类型）字段</p></li>
</ol></li>
<li><p>2023/9/8</p>
<ol>
<li><p>在<a href="../QTYWGZ/HYZTBHSM2/">合约状态变化说明</a>中修改了INE交易所中的合约状态</p></li>
<li><p><a href="../QTYWGZ/GJYSTSZL/">各交易所特殊指令</a>中添加大商所本节有效指令</p></li>
</ol></li>
<li><p>2023/9/5</p>
<ol>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUERYBANKACCOUNTMONEYBYFUTURE.html#anchor-id-01">ReqQueryBankAccountMoneyByFuture</a>增加个别字段必填说明。</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT.html#anchor-id-01">ReqExecOrderInsert</a>中增加faq，各所的行权支持情况</p></li>
</ol></li>
<li><p>2023/8/10</p>
<ol>
<li><p>增加<a href="../QTYWGZ/HYZTBHSM2.html#anchor-id-01">合约状态变化说明</a>中郑商所合约状态是根据5期环境整理的说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-02">ReqOrderInsert</a>新增关于投机套保标志的faq</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION.html#anchor-id-01">ReqOrderAction</a>增加关于未知单撤单的faq</p></li>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-03">ReqOrderInsert</a>关于请求返回的faq</p></li>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION.html#anchor-id-01">OnRspQryInvestorPosition</a>中关于优惠保证金收取规则说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-04">ReqOrderInsert</a>增加CombHedgeFlag的字段说明郑商所只能填写投机标志位</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENT.html#anchor-id-03">OnRspQryInstrument</a>中添加LongMarginRatio、ShortMarginRatio字段说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADINGNOTICE.html#anchor-id-01">OnRtnTradingNotice</a>添加说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENT.html#anchor-id-04">OnRspQryInstrument</a>和<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION.html#anchor-id-02">OnRspQryInvestorPosition</a>添加 PositionDateType和PositionDate字段说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER.html#anchor-id-02">OnRtnOrder</a>添加ZCETotalTradedVolume字段说明</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGEMARGINRATEADJUST.html#anchor-id-01">OnRspQryExchangeMarginRateAdjust</a>添加faq</p></li>
<li><p>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION.html#anchor-id-03">OnRspQryInvestorPosition</a>增加OpenAmount和OpenCost的字段说明</p></li>
<li><p>在<a href="../HQJK/CTHOSTFTDCMDAPI/SUBSCRIBEMARKETDATA.html#anchor-id-01">SubscribeMarketData</a>添加订阅合约faq</p></li>
<li><p>在<a href="../QTYWGZ/TASJS/">TAS介绍</a>中增加升贴水介绍</p></li>
</ol></li>
<li><p>2023/7/17</p>
<ol>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQEXECORDERINSERT/">ReqExecOrderInsert</a>中第二条FAQ</p></li>
<li><p>更新到目前为止<a href="../QTYWGZ/HYZTBHSM2/">合约状态变化说明</a></p></li>
</ol></li>
<li><p>2023/6/2</p>
<ol>
<li>调整<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER.html#anchor-id-01">OnRtnOrder</a>中OrderSubmitStatus字段说明</li>
</ol></li>
<li><p>2023/5/22</p>
<ol>
<li><p>更新版本6.7.0，具体说明见<a href="../6.7.0BBGXSM/">6.7.0版本更新说明</a></p></li>
<li><p>更新<a href="../ZY/">主页</a>说明</p></li>
</ol></li>
<li><p>2023/5/16</p>
<ol>
<li>在<a href="../QTYWGZ/HQSM/">各交易所行情区别</a>添加TrunOver、AveragePrice说明，缺少合约乘数需自行添加至公式中。</li>
</ol></li>
<li><p>2023/3/9</p>
<ol>
<li>添加<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-01">ReqOrderInsert</a>中FAQ对于郑商所报单的说明</li>
</ol></li>
<li><p>2023/3/6</p>
<ol>
<li>修改所有的TradeApi为TraderApi</li>
</ol></li>
<li><p>2022/12/2</p>
<ol>
<li>更新深度行情中OpenInterest的说明<a href="../HQJK/CTHOSTFTDCMDSPI/ONRTNDEPTHMARKETDATA.html#anchor-id-01">OnRtnDepthMarketData</a></li>
</ol></li>
<li><p>2022/11/8</p>
<ol>
<li><p>更新版本6.6.9，具体说明见<a href="../6.6.9BBGXSM/">6.6.9版本更新说明</a></p></li>
<li><p>新增<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODSPBMDETAIL/">ReqQryInvestorProdSPBMDetail</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMINVESTORPORTFDEF/">ReqQrySPBMInvestorPortfDef</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMPORTFDEFINITION/">ReqQrySPBMPortfDefinition</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMINTERPARAMETER/">ReqQrySPBMInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMINTRAPARAMETER/">ReqQrySPBMIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMOPTIONPARAMETER/">ReqQrySPBMOptionParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYSPBMFUTUREPARAMETER/">ReqQrySPBMFutureParameter</a></p></li>
<li><p>新增对应回调<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMFUTUREPARAMETER/">OnRspQrySPBMFutureParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMOPTIONPARAMETER/">OnRspQrySPBMOptionParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTRAPARAMETER/">OnRspQrySPBMIntraParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINTERPARAMETER/">OnRspQrySPBMInterParameter</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMPORTFDEFINITION/">OnRspQrySPBMPortfDefinition</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMINVESTORPORTFDEF/">OnRspQrySPBMInvestorPortfDef</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPORTFMARGINRATIO/">OnRspQryInvestorPortfMarginRatio</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODSPBMDETAIL/">OnRspQryInvestorProdSPBMDetail</a></p></li>
</ol></li>
<li><p>2022/8/25</p>
<ol>
<li><p>修订<a href="../QTYWGZ/QHQQDHQ-ZDCGZ/">期货期权的行权、自对冲</a>中的说明</p></li>
<li><p>删除<a href="../QTYWGZ/DCEZB.html#anchor-id-10">大商所组保</a>中TimeFirstVolume字段是大商所专用的说明</p></li>
<li><p>修订<a href="../QTYWGZ/HYZTBHSM/">合约状态变化说明</a></p></li>
</ol></li>
<li><p>2022/8/23</p>
<ol>
<li><p>更新版本至6.6.8，具体说明见<a href="../6.6.8BBGXSM/">6.6.8版本更新说明</a></p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGIN/">OnRspUserLogin</a>接口结构体有新增广期所时间字段</p></li>
<li><p>新增加页面<a href="../QTYWGZ/QHQQDHQ-ZDCGZ/">期货期权的行权、自对冲规则</a></p></li>
</ol></li>
<li><p>2022/6/20</p>
<ol>
<li><p>新增<a href="../QTYWGZ/JKZYXZYXHSM/">接口中一些重要序号说明</a></p></li>
<li><p>更新版本至6.6.7，具体说明见<a href="../6.6.7BBGXSM/">6.6.7版本更新说明</a></p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTOR/">OnRspQryInvestor</a>和<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYPRODUCT/">OnRspQryProduct</a>接口结构体有新增字段</p></li>
<li><p><a href="../CTSJGSJCJJK/_CTSJGSJCJJK/">看穿式监管数据采集说明</a>中新增<a href="../CTSJGSJCJJK/CTP-GETDATACOLLECTAPIVERSION/">CTP-GetDataCollectApiVersion</a></p></li>
<li><p>更新<a href="../CTSJGSJCJJK/CTP-GETSYSTEMINFO/">CTP-GetSystemInfo</a>中返回值的说明</p></li>
</ol></li>
<li><p>2022/6/8</p>
<ol>
<li>在页面<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYTRADINGACCOUNT.html#anchor-id-01">OnRspQryTradingAccount</a>中添加ReserveBalance和Reserve的说明</li>
</ol></li>
<li><p>2022/4/18</p>
<ol>
<li>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER.html#anchor-id-11">OnRtnOrder</a>中新增faq</li>
</ol></li>
<li><p>2022/4/15</p>
<ol>
<li>在接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYORDER.html#anchor-id-10">OnRspQryOrder</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYTRADE.html#anchor-id-10">OnRspQryTrade</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER.html#anchor-id-10">OnRtnOrder</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE.html#anchor-id-10">OnRtnTrade</a>中新增insertdate和tradedate的faq</li>
</ol></li>
<li><p>2022/4/14</p>
<ol>
<li>在<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYTRADINGACCOUNT/">OnRspQryTradingAccount</a>和<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYSECAGENTTRADINGACCOUNT/">OnRspQrySecAgentTradingAccount</a>中增加已废弃的字段描述</li>
</ol></li>
<li><p>2022/3/8</p>
<ol>
<li>修改<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENT.html#anchor-id-02">OnRspQryInstrument</a>中MinMarketOrderVolume字段说明</li>
</ol></li>
<li><p>2022/3/2</p>
<ol>
<li>修改<a href="../QTYWGZ/BJHXJ.html#anchor-id-01">做市商询价和报价</a>中“是否会撤销前一次报价”行“中金所”为会自动撤销</li>
</ol></li>
<li><p>2022/3/1</p>
<ol>
<li>在<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT.html#anchor-id-01">ReqCombActionInsert</a>中增加示例说明。</li>
</ol></li>
<li><p>2022/2/23</p>
<ol>
<li><p>更新版本至6.6.5</p></li>
<li><p>新增加接口<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYTRADEROFFER/">OnRspQryTraderOffer</a>和<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYTRADEROFFER/">ReqQryTraderOffer</a></p></li>
<li><p>修订<a href="../QTYWGZ/GJYSTSZL/">各交易所特殊指令</a>，删除普通报单说明</p></li>
<li><p>修正<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYACCOUNTREGISTER/">ReqQryAccountregister</a>接口中描述错误，原“填写正确查询无返回”，实际只要签约成功后就能返回。</p></li>
<li><p>更新OrderInsert中<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT.html#anchor-id-05">TimeCondition</a>的字段说明</p></li>
<li><p>新增<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRCOMMRATE/">ReqQryOptionInstrCommRate</a>的<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRCOMMRATE.html#anchor-id-01">faq</a></p></li>
<li><p>更新<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENT.html#anchor-id-01">OnRspQryInstrument</a>中最大最小下单量说明</p></li>
<li><p>更新<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYBROKERTRADINGPARAMS.html#anchor-id-01">ReqQryBrokerTradingParams</a>中查询方法</p></li>
<li><p>新增<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQPARKEDORDERINSERT/">ReqParkedOrderInsert</a>接口关于组合合约预埋单说明</p></li>
<li><p>在报单流控说明中新增<a href="../QTYWGZ/LK.html#anchor-id-01">分用户会话数设置的说明</a></p></li>
<li><p>修改<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQOPTIONSELFCLOSEINSERT/">ReqOptionSelfCloseInsert</a>的Hedgeflag说明改成必填</p></li>
</ol></li>
<li><p>2021/11/3</p>
<ol>
<li><p>修订<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODUCTGROUPMARGIN/">ReqQryInvestorProductGroupMargin</a>中字段注释</p></li>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQAUTHENTICATE/">ReqAuthenticate</a>中faq报错说明</p></li>
</ol></li>
<li><p>2021/8/30</p>
<ol>
<li><p>在<a href="../QTYWGZ/GJYSTSZL.html#anchor-id-04">各交易所特殊指令</a>中金所最优价转限价，五档最优价转限价指令</p></li>
<li><p>在<a href="../CTSJGSJCJJK/CJFAQ.html#anchor-id-05">常见FAQ</a>中新增28点问答</p></li>
</ol></li>
<li><p>2021/8/13</p>
<ol>
<li>新增<a href="../CTSJGSJCJJK/_CTSJGSJCJJK.html#anchor-id-03">看穿式监管数据采集说明</a>中穿透式权限要求说明</li>
</ol></li>
<li><p>2021/7/15</p>
<ol>
<li>新增行情登录接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGIN/">ReqUserLogin</a>的行情登录验证说明</li>
</ol></li>
<li><p>2021/7/13</p>
<ol>
<li><p>新增页面“各家交易所特殊指令”</p></li>
<li><p>新增tas介绍页面中对持仓的说明</p></li>
<li><p>新增<a href="../QTYWGZ/BJHXJ.html#anchor-id-02">做市商询价和报价</a>页面中OrderType和TradeType字段说明</p></li>
<li><p>新增<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>中PositionCost的说明</p></li>
</ol></li>
<li><p>2021/5/21</p>
<ol>
<li><p>更新做市商说明上期所期货合约其他交易所使用接口不同</p></li>
<li><p>6.6.1P1说明中支持订单应为QuoteSysID</p></li>
</ol></li>
<li><p>2021/5/10</p>
<ol>
<li><p>更新6.6.1P1版本说明</p></li>
<li><p>修正<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRTRADECOST/">ReqQryOptionInstrTradeCost</a>接口InvestorID字段可作为过滤条件</p></li>
<li><p>修正<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYOPTIONINSTRTRADECOST/">ReqQryOptionInstrTradeCost</a>接口InputPrice和UnderlyingPrice中文解释错误问题</p></li>
<li><p>修正流控说明页在途流控描述不准确问题，原在未收到响应前，不能发起下一笔查询请求 改为 在未收完所有的查询响应前，不能发起下一笔查询请求 </p></li>
</ol></li>
<li><p>2021/3/1</p>
<ol>
<li>行情<a href="../HQJK/CTHOSTFTDCMDAPI/CREATEFTDCMDAPI/">CreateFtdcMdApi</a>添加通过tcp、udp、组播模式连接mdfront的说明</li>
</ol></li>
<li><p>2021/1/25</p>
<ol>
<li><p>新增页面<a href="../6.5.1BBGXSMBCSM/">6.5.1版本更新说明补充说明</a></p></li>
<li><p>对<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYCLASSIFIEDINSTRUMENT/">ReqQryClassifiedInstrument</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>添加说明</p></li>
</ol></li>
<li><p>2021/1/6</p>
<ol>
<li>修正<a href="../6.5.1BBGXSM/">6.5.1版本更新说明</a>中运行环境说明，windows支持32位和64位。</li>
</ol></li>
<li><p>2020/12/24</p>
<ol>
<li><p>添加brokerid在认证中是必填字段</p></li>
<li><p>6.5.1中ipv6说明RegisterFens-&gt;RegisterNmaeServer修订</p></li>
<li><p><a href="../ZY/">主页</a>添加线程数说明</p></li>
</ol></li>
<li><p>2020/12/10</p>
<ol>
<li><p>调整Tas手续费和保证金说明</p></li>
<li><p>修改<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNBULLETIN/">OnRtnBulletin</a>说明属于公有流</p></li>
<li><p>修改<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRTNINSTRUMENTSTATUS/">OnRtnInstrumentStatus</a>问答</p></li>
<li><p>调整<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENT/">ReqQryInstrument</a>中FAQ说明</p></li>
<li><p>调整ReqQueryMaxOrderVolume名称为<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUERYMAXORDERVOLUME/">ReqQryMaxOrderVolume</a></p></li>
<li><p>增加<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONFRONTDISCONNECTED/">OnFrontDisconnected</a>说明</p></li>
<li><p>“<a href="../QTYWGZ/BJHXJ/">做市商询价和报价</a>”页面对于是否会撤销前一次报价说明增加七期说明</p></li>
<li><p><a href="../QTYWGZ/DCEZB/">大商所组保</a>合约名称修改BUL-&gt;BLS   BER-&gt;BES</p></li>
<li><p><a href="../ZY/">主页</a>增加字符集说明</p></li>
<li><p>增加Ref字段需要递增说明</p></li>
<li><p>对于银期转账中TradeCode说明修改。</p></li>
<li><p><a href="../JYJK/CTHOSTFTDCTRADERSPI/SUBSCRIBEPUBLICTOPIC/">SubscribePublicTopic</a>增加一种私有流方式</p></li>
<li><p>“<a href="../QTYWGZ/DCEZB/">大商所组保</a>”增加FAQ说明</p></li>
</ol></li>
<li><p>2020/11/6</p>
<ol>
<li><p>增加各个接口对ipv6的说明</p></li>
<li><p>修订<a href="../JYJK/CTHOSTFTDCTRADERSPI/REGISTERUSERSYSTEMINFO/">RegisterUserSystemInfo</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/SUBMITUSERSYSTEMINFO/">SubmitUserSystemInfo</a>接口字段说明</p></li>
</ol></li>
<li><p>2020/10/21</p>
<ol>
<li><p>更新6.5.1apichm说明</p></li>
<li><p>新增6.5.1api版本说明</p></li>
<li><p>新增两个接口<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYCLASSIFIEDINSTRUMENT/">ReqQryClassifiedInstrument</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQRYCOMBPROMOTIONPARAM/">ReqQryCombPromotionParam</a>对应的回调<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYCLASSIFIEDINSTRUMENT/">OnRspQryClassifiedInstrument</a>、<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYCOMBPROMOTIONPARAM/">OnRspQryCombPromotionParam</a></p></li>
<li><p>ReqQueryMaxOrderVolume接口修改为<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQQUERYMAXORDERVOLUME/">ReqQryMaxOrderVolume</a>，对应的回调OnRspQueryMaxOrderVolume修改为<a href="../JYJK/CTHOSTFTDCTRADERAPI/SM/">OnRspQryMaxOrderVolume</a></p></li>
</ol></li>
<li><p>2020/04/29</p>
<ol>
<li><p>更新到6.3.19 api说明，更新对应新增字段。</p></li>
<li><p>新增tas介绍</p></li>
<li><p>新增fens介绍</p></li>
<li><p>更正代码示例错误，<a href="../HQJK/CTHOSTFTDCMDAPI/RELEASE/">Release</a>()前使用<a href="../JYJK/CTHOSTFTDCTRADERSPI/REGISTERSPI/">RegisterSpi</a>(NULL)，这个代码是错误的，会导致api概率崩溃。</p></li>
<li><p>新增<a href="../HQJK/CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>、<a href="../JYJK/CTHOSTFTDCTRADERSPI/REQAUTHENTICATE/">ReqAuthenticate</a>、增加流控参数部分说明、郑商所行情说明。</p></li>
</ol></li>
<li><p>2020/03/13</p>
<ol>
<li>新增init/release线程安全说明</li>
</ol></li>
<li><p>2020/03/06</p>
<ol>
<li>修正logout之后是否会触发重连机制</li>
</ol></li>
<li><p>2020/02/21</p>
<ol>
<li><p>新添加<a href="../QTYWGZ/SJLSM/">通讯模式</a>中基本接口所属的数据流</p></li>
<li><p>完善做市商接受询价的说明</p></li>
<li><p>修改对于撤单接口就上期所新增挂单激活操作在本系统是否支持说明</p></li>
<li><p>新增条件单说明</p></li>
<li><p>新增各个交易所盘中行情合约状态推送的具体状态</p></li>
</ol></li>
<li><p>2019/11/28</p>
<ol>
<li><p>新增<a href="../QTYWGZ/BJHXJ/">做市商询价和报价</a>指令介绍</p></li>
<li><p>修正<a href="../HQJK/CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>中FAQ回答错误。普通投资者只能订阅上期所和中金所询价通知 改为 普通投资者能订阅四所的询价通知。</p></li>
</ol></li>
<li><p>2019/07/12</p>
<ol>
<li>新增<a href="../QTYWGZ/DBHB/">报单回调规则</a>、<a href="../QTYWGZ/DJHDGZ/">报价回调规则</a></li>
</ol></li>
<li><p>2019/07/03</p>
<ol>
<li>新增相关穿透式的一些问题回答</li>
</ol></li>
<li><p>2019/06/27</p>
<ol>
<li><p>新增<a href="../QTYWGZ/DCEZB/">大商所组保</a>业务说明</p></li>
<li><p>修正<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITION/">OnRspQryInvestorPosition</a>和<a href="../JYJK/CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPOSITIONDETAIL/">OnRspQryInvestorPositionDetail</a>里缺失TimeFirstVolume和PositionCostOffset字段的问题</p></li>
</ol></li>
<li><p>2019/06/05</p>
<ol>
<li>新增CTP流控说明</li>
</ol></li>
<li><p>2019/05/27</p>
<ol>
<li><p>新增<a href="../JYJK/_JYJK/">交易接口</a>和<a href="../HQJK/_HQJK/">行情接口</a>代码示例说明。</p></li>
<li><p>新增<a href="../YDZY/">阅读指引</a>，方便用户快速上手chm文档。</p></li>
</ol></li>
<li><p>2019/04/29</p>
<ol>
<li>新增看穿式监管数据采集的<a href="../CTSJGSJCJJK/CJFAQ/">常见FAQ</a>。</li>
</ol></li>
<li><p>2019/4/11</p>
<ol>
<li>新增二代行情API接口说明，该API新增接口QryMulticastInstrument。</li>
</ol></li>
<li><p>2019/3/14</p>
<ol>
<li><p>增加看穿式监管相关API接口的返回值。</p></li>
<li><p><a href="../ZY/">主页</a>新增版本兼容性说明，务必了解！</p></li>
</ol></li>
<li><p>2019/3/14</p>
<ol>
<li>增加有关看穿式监管相关问题接单。</li>
</ol></li>
</ul>
