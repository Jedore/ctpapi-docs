<p>报单操作错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="8586a018-cbde-43c3-81b9-a62a15a0767e"></span>
## 1.函数原型
<p>virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="b2867210-0ccb-4fe3-a37e-5faa3a9a55d9"></span>
## 2.参数
<p>pOrderAction：报单操作</p>
<pre><code>struct CThostFtdcOrderActionField
{
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///投资者代码
TThostFtdcInvestorIDType    InvestorID;
///报单操作引用
TThostFtdcOrderActionRefType    OrderActionRef;
///报单引用
TThostFtdcOrderRefType  OrderRef;
///请求编号
TThostFtdcRequestIDType RequestID;
///前置编号
TThostFtdcFrontIDType   FrontID;
///会话编号
TThostFtdcSessionIDType SessionID;
///交易所代码
TThostFtdcExchangeIDType    ExchangeID;
///报单编号
TThostFtdcOrderSysIDType    OrderSysID;
///操作标志
TThostFtdcActionFlagType    ActionFlag;
///价格
TThostFtdcPriceType LimitPrice;
///数量变化
TThostFtdcVolumeType    VolumeChange;
///操作日期
TThostFtdcDateType  ActionDate;
///操作时间
TThostFtdcTimeType  ActionTime;
///交易所交易员代码
TThostFtdcTraderIDType  TraderID;
///安装编号
TThostFtdcInstallIDType InstallID;
///本地报单编号
TThostFtdcOrderLocalIDType  OrderLocalID;
///操作本地编号
TThostFtdcOrderLocalIDType  ActionLocalID;
///会员代码
TThostFtdcParticipantIDType ParticipantID;
///客户代码
TThostFtdcClientIDType  ClientID;
///业务单元
TThostFtdcBusinessUnitType  BusinessUnit;
///报单操作状态
TThostFtdcOrderActionStatusType OrderActionStatus;
///用户代码
TThostFtdcUserIDType    UserID;
///状态信息
TThostFtdcErrorMsgType  StatusMsg;
///保留的无效字段
TThostFtdcOldInstrumentIDType   reserve1;
///营业部编号
TThostFtdcBranchIDType  BranchID;
///投资单元代码
TThostFtdcInvestUnitIDType  InvestUnitID;
///保留的无效字段
TThostFtdcOldIPAddressType  reserve2;
///Mac地址
TThostFtdcMacAddressType    MacAddress;
///合约代码
TThostFtdcInstrumentIDType  InstrumentID;
///IP地址
TThostFtdcIPAddressType IPAddress;
///报单回显字段
TThostFtdcOrderMemoType OrderMemo;
///session上请求计数 api自动维护
TThostFtdcSequenceNo12Type  SessionReqSeq;
};
</code></pre>
<p>OrderSysID：交易所返回的报单编号</p>
<p>ActionFlag：撤单标志，现在只支持删除，不支持修改</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="a47c82a7-492e-49be-8795-92e91d47a7d2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="881055ec-97f1-4051-b289-081bff0d95aa"></span>
## 4.FAQ
<p>无</p>
