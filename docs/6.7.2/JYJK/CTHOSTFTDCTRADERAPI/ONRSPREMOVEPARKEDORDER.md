<p>删除预埋单响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQREMOVEPARKEDORDER/">ReqRemoveParkedOrder</a>后，该方法被调用。</p>
<span class="anchor" id="971aa93e-8694-4d26-836b-fe88b67af491"></span>
## 1.函数原型
<p>virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="17e13201-1b68-4c38-a2fd-b5273bfcacc1"></span>
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
<span class="anchor" id="1b554335-2cc7-483a-b1c0-26ca3243e871"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c7e22f27-1e37-4de7-bd1f-4d9992f15e5d"></span>
## 4.FAQ
<p>无</p>
