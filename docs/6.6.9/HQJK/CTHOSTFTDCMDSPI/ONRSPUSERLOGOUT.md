<p>登出请求响应，当<a href="../../CTHOSTFTDCMDAPI/REQUSERLOGOUT/">ReqUserLogout</a>后，该方法被调用。</p>
<span class="anchor" id="f50a4ced-4465-4e37-8d5d-d4bf5b951dd7"></span>
## 1.函数原型
<p>virtual void <a href="../../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPUSERLOGOUT/">OnRspUserLogout</a>(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0cc0f5aa-7046-47a1-bf9f-1a9b94ca7cdb"></span>
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
<span class="anchor" id="718813e0-c6da-4573-b3b6-2049968c63f5"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6782e90e-af13-47f8-80ad-5031cc97dceb"></span>
## 4.FAQ
<p>无</p>
