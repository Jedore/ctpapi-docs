<p>请求查询询价响应，当执行ReqQryForQuote后，该方法被调用。</p>
<span class="anchor" id="2e412f5d-ce6f-4af0-9fad-ef3a39fd3f88"></span>
## 1.函数原型
<p>virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5a626e57-d867-410d-999b-f9cac0082c0c"></span>
## 2.参数
<p>pForQuote：询价</p>
<pre><code>struct CThostFtdcForQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价引用
    TThostFtdcOrderRefType ForQuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///本地询价编号
    TThostFtdcOrderLocalIDType ForQuoteLocalID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///客户代码
    TThostFtdcClientIDType ClientID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///交易所交易员代码
    TThostFtdcTraderIDType TraderID;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///报单日期
    TThostFtdcDateType InsertDate;
    ///插入时间
    TThostFtdcTimeType InsertTime;
    ///询价状态
    TThostFtdcForQuoteStatusType ForQuoteStatus;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///状态信息
    TThostFtdcErrorMsgType StatusMsg;
    ///操作用户代码
    TThostFtdcUserIDType ActiveUserID;
    ///经纪公司询价编号
    TThostFtdcSequenceNoType BrokerForQutoSeq;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="4429e420-6a71-4f43-9af3-09f19a7e5149"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1f02864b-4df0-48c4-8d5b-101d8e3786ad"></span>
## 4.FAQ
<p>无</p>
