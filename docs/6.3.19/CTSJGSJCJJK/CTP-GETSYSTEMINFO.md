<p>获取AES加密和RSA加密的终端信息。该函数来自采集终端信息的动态链接库（安卓版的函数名和使用方法较windows和linux有所区别，请注意阅读API包相关说明文档）。</p>
<p>仅中继模式下的客户端需要调用此函数来采集信息。中继需要将客户端采集到的信息上报给CTP。</p>
<p>直连模式下，登录的时候自动采集并上报终端信息，所以无需调用。</p>
<blockquote>
<p>采集库在win、linux、android上不是线程安全的，不要并发调用，ios是线程安全的</p>
</blockquote>
<span class="anchor" id="6f4dace7-160e-454d-9640-28965439ec5e"></span>
## 1.函数原型
<p>int CTP_GetSystemInfo(char* pSystemInfo, int&amp; nLen);</p>
<span class="anchor" id="8ad1ab0b-61c9-4d56-abc0-a095582eb0c4"></span>
## 2.参数
<p>pSystemInfo：空间需要调用者自己分配至少270个字节。</p>
<blockquote>
<p>要注意这并不是一个字符串，而是数组，因为多次加密后可能断串，<strong>使用memcpy拷贝值而不是strcpy</strong>。</p>
</blockquote>
<p>nLen：获取到的采集信息的长度。</p>
<span class="anchor" id="1963549a-25d9-41ac-9c8d-58615eedb41e"></span>
## 3.返回
<p>0 为正确，非0为错误。</p>
<span class="anchor" id="d123236e-af01-438d-a10d-27a9b8fddade"></span>
## 4.调用示例
<pre><code>char pSystemInfo[344];
int len;
CTP_GetSystemInfo(pSystemInfo, len);
</code></pre>
<span class="anchor" id="deaee2bd-a69f-469a-8958-2357501418d9"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">终端采集到的信息，保存到数据库里后显示为乱码，怎么办？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>可以使用BASE64转码成可见字符后再存储。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在windows下调用该函数后，控制台窗口打印出一些日志，提示找不到wmic之类的信息，这个有关系吗？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>有关系，采集函数需要调用相关windows组件来采集设备信息，如果没有对应组件，则会采集不到相应信息，不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">在linux下调用该函数后，控制台窗口会输出一些报错日志，提示没有权限之类的错误，这个有关系吗？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>有关系，采集函数需要调用linux命令来采集设备信息，如果没有对应权限，则会采集不到相应信息，不符合监管要求。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
