<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="182c77ee-de6a-43ed-849b-1c48ac2b150b"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f300ea67-3bc8-490d-a1f0-1c677c85f3c0"></span>
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
<span class="anchor" id="2d9ebced-c0b8-41c7-9007-8c8df1037ae6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="411837cf-bd1b-4525-af20-8057d2d03741"></span>
## 4.FAQ
<p>无</p>
