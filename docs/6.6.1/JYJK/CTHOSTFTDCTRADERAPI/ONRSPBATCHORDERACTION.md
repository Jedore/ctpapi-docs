<p>批量报单操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQBATCHORDERACTION/">ReqBatchOrderAction</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="310e0d3e-a136-40e6-8bb4-7b616a523f3f"></span>
## 1.函数原型
<p>virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="dc276b5e-915c-4dae-aff2-be501135aae2"></span>
## 2.参数
<p>pInputBatchOrderAction：输入批量报单操作</p>
<pre><code>struct CThostFtdcInputBatchOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报单操作引用
    TThostFtdcOrderActionRefType    OrderActionRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve1;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="a6616ea3-d7a4-49c4-ab45-82e22258d191"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fedb4d6f-32a6-4f3d-a845-6d2514b33255"></span>
## 4.FAQ
<p>无</p>
