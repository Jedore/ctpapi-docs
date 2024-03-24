<p>登出请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQUSERLOGOUT/">ReqUserLogout</a>后，该方法被调用。</p>
<span class="anchor" id="98b5fa61-60fe-4306-82c0-fd67da64b999"></span>
## 1.函数原型
<p>virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="546ea254-9585-43af-ae38-3f958e584669"></span>
## 2.参数
<p>pUserLogout:用户登出请求</p>
<pre><code>struct CThostFtdcUserLogoutField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///用户代码
    TThostFtdcUserIDType UserID;
};
</code></pre>
<p>pRspInfo:响应信息</p>
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
<span class="anchor" id="87c1b36c-dda0-4282-959e-8b67eabfbacd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="15e8545e-e55e-4bfc-9865-343741c90312"></span>
## 4.FAQ
<p>无</p>
