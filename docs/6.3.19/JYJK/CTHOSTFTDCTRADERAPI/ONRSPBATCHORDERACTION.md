<p>批量报单操作请求响应，当执行ReqBatchOrderAction后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="f7f5ae8b-89ac-401b-aa4f-7cb919397393"></span>
## 1.函数原型
<p>virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2dd70147-df21-43b0-9769-5342f11b9b8d"></span>
## 2.参数
<p>pInputBatchOrderAction：输入批量报单操作</p>
<pre><code>struct CThostFtdcInputBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///用户代码
    TThostFtdcUserIDType UserID;
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
<span class="anchor" id="e1c5b0ed-fdc9-4be4-9781-2e07f1afdd95"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2068f4db-5262-4044-8e9c-3b701be255e5"></span>
## 4.FAQ
<p>无</p>
