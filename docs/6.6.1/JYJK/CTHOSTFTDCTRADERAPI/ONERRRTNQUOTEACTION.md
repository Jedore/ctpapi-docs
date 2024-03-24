<p>报价操作错误回报, 当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUOTEACTION/">ReqQuoteAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="0614019b-cf3f-4efc-9020-d2309a544f81"></span>
## 1.函数原型
<p>virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="e3421d67-4528-4b09-a7f5-0f7bb0ab0d35"></span>
## 2.参数
<p>pQuoteAction：报价操作</p>
<pre><code>struct CThostFtdcQuoteActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报价操作引用
    TThostFtdcOrderActionRefType    QuoteActionRef;
    ///报价引用
    TThostFtdcOrderRefType  QuoteRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///报价操作编号
    TThostFtdcOrderSysIDType    QuoteSysID;
    ///操作标志
    TThostFtdcActionFlagType    ActionFlag;
    ///操作日期
    TThostFtdcDateType  ActionDate;
    ///操作时间
    TThostFtdcTimeType  ActionTime;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///本地报价编号
    TThostFtdcOrderLocalIDType  QuoteLocalID;
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
};
</code></pre>
<p>OrderActionStatus：报价撤销的状态信息，此处返回的是错误信息</p>
<p>StatusMsg：报价单最后的状态</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="283c27c3-9afd-4904-82c1-9b64b9f1a879"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a5fb9cf2-bcff-4ccb-b1ec-3aafc0a82db2"></span>
## 4.FAQ
<p>无</p>
