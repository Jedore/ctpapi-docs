<p>查询用户当前支持的认证模式的回复</p>
<span class="anchor" id="0ea231ee-074c-4dba-a091-cc8c0bc1b4bb"></span>
## 1.函数原型
<p>virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="37bef859-1012-40e6-a040-9ed0a16b62d6"></span>
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
<span class="anchor" id="b77df6f8-4f51-46ec-8082-8844432ac74d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="dcbaf5c4-260b-49d1-8f99-3084ef54bf67"></span>
## 4.FAQ
<p>无</p>
