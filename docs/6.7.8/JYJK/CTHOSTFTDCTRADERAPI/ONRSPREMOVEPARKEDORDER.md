<p>删除预埋单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a>后，该方法被调用。</p>
<span class="anchor" id="e018ab00-a43e-42d8-8a73-d2f2034b07e0"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0d7d0b5b-1067-4af2-994a-d53db40ed19f"></span>
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
<span class="anchor" id="c841e2da-6a16-4c38-b332-c67e1b45866b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="cf55f0c2-55a1-4ef4-a4f6-88aca3981c7f"></span>
## 4.FAQ
<p>无</p>
