<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="ba1fd251-ad39-42e7-b249-25f0b9430bf5"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="aa6ed4de-9f3b-443b-a4e2-8835c986b291"></span>
## 2.参数
<p>pRspUserAuthMethod：用户发出获取安全安全登陆方法回复</p>
<pre><code>struct CThostFtdcRspUserAuthMethodField
{
    ///当前可以用的认证模式
    TThostFtdcCurrentAuthMethodType UsableAuthMethod;
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
<span class="anchor" id="8b98704f-6e61-4566-aaf9-c5f9cd3f577a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="7b5c5001-a5d0-4de0-9eda-1bec343dc06f"></span>
## 4.FAQ
<p>无</p>
