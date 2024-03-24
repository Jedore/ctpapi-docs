<p>删除预埋单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a>后，该方法被调用。</p>
<span class="anchor" id="75ff3a00-e318-43ad-a9dc-15ec9084e947"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="93bdfc2d-72f8-4a41-ac9f-7050e3d43b98"></span>
## 2.参数
<p>pRemoveParkedOrder：删除预埋单</p>
<pre><code>struct CThostFtdcRemoveParkedOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///预埋报单编号
    TThostFtdcParkedOrderIDType ParkedOrderID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="fc968fa7-1196-4cca-9017-88c059b4ed11"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6e88824a-4222-4fe7-b72d-4b103b85a861"></span>
## 4.FAQ
<p>无</p>
