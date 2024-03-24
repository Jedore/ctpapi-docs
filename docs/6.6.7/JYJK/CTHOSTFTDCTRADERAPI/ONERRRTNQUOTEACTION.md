<p>报价操作错误回报, 当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUOTEACTION/">ReqQuoteAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="dba8520e-b8d3-4fdd-aa6a-4f68fd1bcc41"></span>
## 1.函数原型
<p>virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="176b54b6-daf1-4359-931f-245c85548c61"></span>
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
<span class="anchor" id="bcac8585-93df-4302-ad0c-f5dca6629921"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7c78ffa4-40af-4873-a622-a231fa22fa65"></span>
## 4.FAQ
<p>无</p>
