<p>申请组合通知，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT/">ReqCombActionInsert</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="0ad034de-70e2-49df-8a88-db6400aac3dd"></span>
## 1.函数原型
<p>virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {};</p>
<span class="anchor" id="e73ae424-9a9e-4fd2-bce8-cd6af3036b24"></span>
## 2.参数
<p>pCombAction：申请组合</p>
<pre><code>struct CThostFtdcCombActionField
{
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///投资者代码
TThostFtdcInvestorIDType    InvestorID;
///保留的无效字段
TThostFtdcOldInstrumentIDType   reserve1;
///组合引用
TThostFtdcOrderRefType  CombActionRef;
///用户代码
TThostFtdcUserIDType    UserID;
///买卖方向
TThostFtdcDirectionType Direction;
///数量
TThostFtdcVolumeType    Volume;
///组合指令方向
TThostFtdcCombDirectionType CombDirection;
///投机套保标志
TThostFtdcHedgeFlagType HedgeFlag;
///本地申请组合编号
TThostFtdcOrderLocalIDType  ActionLocalID;
///交易所代码
TThostFtdcExchangeIDType    ExchangeID;
///会员代码
TThostFtdcParticipantIDType ParticipantID;
///客户代码
TThostFtdcClientIDType  ClientID;
///保留的无效字段
TThostFtdcOldExchangeInstIDType reserve2;
///交易所交易员代码
TThostFtdcTraderIDType  TraderID;
///安装编号
TThostFtdcInstallIDType InstallID;
///组合状态
TThostFtdcOrderActionStatusType ActionStatus;
///报单提示序号
TThostFtdcSequenceNoType    NotifySequence;
///交易日
TThostFtdcDateType  TradingDay;
///结算编号
TThostFtdcSettlementIDType  SettlementID;
///序号
TThostFtdcSequenceNoType    SequenceNo;
///前置编号
TThostFtdcFrontIDType   FrontID;
///会话编号
TThostFtdcSessionIDType SessionID;
///用户端产品信息
TThostFtdcProductInfoType   UserProductInfo;
///状态信息
TThostFtdcErrorMsgType  StatusMsg;
///保留的无效字段
TThostFtdcOldIPAddressType  reserve3;
///Mac地址
TThostFtdcMacAddressType    MacAddress;
///组合编号
TThostFtdcTradeIDType   ComTradeID;
///营业部编号
TThostFtdcBranchIDType  BranchID;
///投资单元代码
TThostFtdcInvestUnitIDType  InvestUnitID;
///合约代码
TThostFtdcInstrumentIDType  InstrumentID;
///合约在交易所的代码
TThostFtdcExchangeInstIDType    ExchangeInstID;
///IP地址
TThostFtdcIPAddressType IPAddress;
};
</code></pre>
<p>InstallID：CTP内部使用</p>
<p>ActionStatus：报入组合后的报单状态</p>
<span class="anchor" id="541065e6-b5b4-4de8-8f5c-1f03af12fb98"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d1a3924c-c692-42d6-9c00-b534e6f49d65"></span>
## 4.FAQ
<p>无</p>
