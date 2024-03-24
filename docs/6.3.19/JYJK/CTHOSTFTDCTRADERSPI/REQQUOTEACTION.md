<p>报价操作请求，用于撤销报价</p>
<p>错误响应:OnRspQuoteAction   OnErrRtnQuoteAction</p>
<p>正确响应:OnRtnQuote  OnRtnOrder</p>
<span class="anchor" id="ed8306cb-0fb2-48c7-a47a-4013d2a241a0"></span>
## 1.函数原型
<p>virtual int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) = 0;</p>
<span class="anchor" id="51675470-2f6b-466f-b561-239562710d14"></span>
## 2.参数
<p>pInputQuoteAction：输入报价操作</p>
<pre><code>struct CThostFtdcInputQuoteActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报价操作引用
    TThostFtdcOrderActionRefType QuoteActionRef;
    ///报价引用
    TThostFtdcOrderRefType QuoteRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报价操作编号
    TThostFtdcOrderSysIDType QuoteSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>FrontID：对应要撤销的报价的前置编号</p>
<p>SessionID：对应要撤销的报价的会话编号</p>
<p>QuoteSysID: 对应要撤销的报价的编号</p>
<p>ActionFlag：操作标志，支持删除，目前不支持改单。想实现改单操作可以先撤销之后再重新报单。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="0904f8d6-eade-4f40-88d6-4ffdf252e606"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="080bf848-388f-4a9d-8c92-e0b25cd3580f"></span>
## 4.调用示例
<pre><code>CThostFtdcInputQuoteActionField t = { 0 };
strcpy_s(t.BrokerID, "9999");
strcpy_s(t.InvestorID, "1000001");
strcpy_s(t.UserID, "1000001");
strcpy_s(t.ExchangeID, "SHFE");
strcpy_s(t.QuoteRef, "           1");
t.FrontID = 1;
t.SessionID = 6442531;
t.ActionFlag = THOST_FTDC_AF_Delete;
strcpy_s(t.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQuoteAction(&amp;t, nRequestID++);
</code></pre>
<span class="anchor" id="49328d66-6131-4884-8071-e6bfe16cd7db"></span>
## 5.FAQ
<p>无</p>
