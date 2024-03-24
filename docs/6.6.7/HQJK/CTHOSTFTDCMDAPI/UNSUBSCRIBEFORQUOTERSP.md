<p>退订询价，对应响应<a href="../../CTHOSTFTDCMDSPI/ONRSPUNSUBFORQUOTERSP/">OnRspUnSubForQuoteRsp</a></p>
<span class="anchor" id="a5c18d42-1c51-46eb-bb09-368f8e8a131e"></span>
## 1.函数原型
<p>virtual int UnSubscribeForQuoteRsp(char *ppInstrumentID[], int nCount) = 0;</p>
<span class="anchor" id="3b126854-21c7-404f-8966-3d6a1285ab43"></span>
## 2.参数
<p>ppInstrumentID：合约ID</p>
<p>nCount：要订阅/退订行情的合约个数</p>
<span class="anchor" id="9b1be195-b9dc-405b-b34c-6ee005297216"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6ac420d6-ddb3-4103-a4a6-89db9c492841"></span>
## 4.调用示例
<pre><code>char **ppInstrumentID = new char*[50];
ppInstrumentID[0] = “sc1801”;
m_pUserMdApi-&gt;SubscribeForQuoteRsp(ppInstrumentID, 1);
</code></pre>
<span class="anchor" id="065beea5-9bd9-48d0-b1f3-9fc57058dde8"></span>
## 5.FAQ
<p>无</p>
