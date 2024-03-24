<p>登出请求响应，当<a href="../../../JYJK/CTHOSTFTDCTRADERSPI/REQUSERLOGOUT/">ReqUserLogout</a>后，该方法被调用。</p>
<span class="anchor" id="2496f319-b918-4589-b574-d781651699e5"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7056545f-c779-4f48-b5bc-562a3f6841de"></span>
## 2.参数
<p>pUserLogout：用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
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
<p>nRequestID：返回用户操作请求的ID，该ID由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="2d9d126e-e19f-496c-bb97-1425ca4a198a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2b53ca12-df28-4415-b693-d7bdd1cc305a"></span>
## 4.FAQ
<p>无</p>
